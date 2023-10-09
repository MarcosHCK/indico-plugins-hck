# Copyright 2023 MarcosHCK
# This file is part of PaymentTransfermovil.
#
# PaymentTransfermovil is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PaymentTransfermovil is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PaymentTransfermovil. If not, see <http://www.gnu.org/licenses/>.
#
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from flask import flash, redirect, request
from flask_pluginengine import current_plugin, render_plugin_template
from indico.core.plugins import url_for_plugin
from indico.modules.events.payment.models.transactions import TransactionAction, TransactionStatus
from indico.modules.events.payment.util import register_transaction
from indico.modules.events.registration.models.registrations import Registration
from indico.web.flask.util import NotFound
from indico.web.rh import RH
from io import BytesIO
from qrcode.image import svg
from werkzeug.exceptions import BadRequest, InternalServerError
import base64, os, qrcode, requests, time

def _deserialize_password (password : str) -> bytes:
  return base64.b64decode (password.encode ('utf-8'))

def _serialize_password (password : bytes) -> str:
  return base64.b64encode (password).decode ('utf-8')

class RHTransfermovil (RH):

  CSRF_ENABLED = False

  def _check_nonce (self, salt, nonce):
    pswd = self._gen_noce_password ()
    algo = PBKDF2HMAC (algorithm = hashes.SHA256 (), length = 128, salt = salt, iterations = 480000)
    return algo.verify (pswd, nonce)

  def _is_duplicated (self):
    transaction = self.registration.transaction
    return (not not transaction) and (transaction.provider == 'transfermovil')

  def _gen_nonce (self, salt):
    pswd = self._gen_noce_password ()
    algo = PBKDF2HMAC (algorithm = hashes.SHA256 (), length = 128, salt = salt, iterations = 480000)
    return algo.derive (pswd)

  def _gen_noce_password (self):
    sourceid = self._get_source_id ()
    username = self._get_user_name ()

    password = '{0}-{1}-{2}'.format (sourceid, username, self.token)
    return password.encode ('utf-8')

  def _get_source_id (self):
    if (current_plugin.event_settings.get (self.registration.registration_form.event, 'source_id') == None):
      return current_plugin.settings.get ('source_id')
    else:
      return current_plugin.event_settings.get (self.registration.registration_form.event, 'source_id')

  def _get_url (self):
    return current_plugin.settings.get ('url')

  def _get_user_name (self):
    if (current_plugin.event_settings.get (self.registration.registration_form.event, 'user_name') == None):
      return current_plugin.settings.get ('user_name')
    else:
      return current_plugin.event_settings.get (self.registration.registration_form.event, 'user_name')

  def _process_args (self):
    self.token = request.args ['token']
    self.registration = Registration.query.filter_by (uuid = self.token).first ()

    if not self.registration:
      raise BadRequest ()

  def _register (self, action, data):

    register_transaction (
      action = action,
      amount = self.amount,
      currency = self.currency,
      data = data,
      provider = 'transfermovil',
      registration = self.registration)

class RHTransfermovilNotify (RHTransfermovil):

  def _is_duplicated (self):
    status = TransactionStatus.pending
    transaction = self.registration.transaction
    return super ()._is_duplicated () and (transaction.status != status)

  def _process (self):
    if (self._is_duplicated ()):
      current_plugin.logger.info("Payment not recorded because transaction was duplicated\nData received: %s",
                                    request.json)
      raise BadRequest ()
    else:

      if (not request.headers.has_key ('password')):
        raise BadRequest ()
      if (request.headers.get ('source') != self._get_source_id ()):
        raise BadRequest ()
      if (request.headers.get ('username') != self._get_user_name ()):
        raise BadRequest ()

      notify = request.json

      if (notify.get ('ExternalId') != self.token):
        raise BadRequest ()
      if (notify.get ('Source') != self._get_source_id ()):
        raise BadRequest ()

      nonce = request.headers.get ('password')
      transaction = self.registration.transaction

      if (not self._check_nonce (transaction.data ['salt'], nonce)):
        raise BadRequest ()

      data = {
          'Bank' : notify.get ('Bank'),
          'bank_id' : notify.get ('BankId'),
          'phone' : notify.get ('Phone'),
          'tm_id' : notify.get ('TmId'),
        }

      self.amount = transaction.amount
      self.currency = transaction.currency

      self._register (TransactionAction.complete, data)
      return { "Success" : True, "Resultmsg" : "OK", "Status" : 1, }

class RHTransfermovilProceed (RHTransfermovil):

  def _process (self):

    if (self._is_duplicated ()):
      current_plugin.logger.info("Payment not recorded because transaction was duplicated\nData received: %s",
                                       request.json)
      raise BadRequest ()
    else:

      salt = os.urandom (16)
      nonce = self._gen_nonce (salt)

      notify_url = url_for_plugin ('payment_transfermovil.notify', self.registration.locator.uuid, _external = True)

      body = {
          'request' : {
              'Amount' : self.amount,
              'Currency' : self.currency,
              'Description' : "Indico Event Payment",
              'ExternalId' : self.token,
              'Source' : self._get_source_id (),
              'UrlResponse' : notify_url,
              'ValidTime' : 60 * (10),
            }
        }

      headers = {
          'password' : _serialize_password (nonce),
          'source' : self._get_source_id (),
          'username' : self._get_user_name (),
        }

      result = requests.post (self._get_url (), headers = headers, json = body)

      if (not result.ok):
        current_plugin.logger.warning ("Transfermovil API request error: %i %s", result.status_code, result.reason)
        raise InternalServerError ()
      else:

        response = result.json ().get ('PayOrderResult')

        if (response.get ('Success') != 'true'):
          current_plugin.logger.warning ("Transfermovil API request error: failed method")
          raise InternalServerError ()
        else:

          self._register (TransactionAction.pending, { 'order_id' : response.get ('OrderId'), 'salt' : _serialize_password (salt), })

          json = '{{ "id_transaccion" : "{id}", "importe" : {amount}, "moneda" : {currency}, "numero_proveedor" : {source_id}, "version" : 1, }}'
          json = json.format (amount = self.amount, currency = self.currency, id = response.get ('OrderId'), source_id = self._get_source_id ())

          stream = BytesIO ()
          qr = qrcode.make (json, image_factory = qrcode.image.svg.SvgImage)
          qr.save (stream)

          return { "qr" : base64.b64encode (stream.getvalue ()).decode (), }

  def _process_args (self):
    super ()._process_args ()
    self.amount = request.json.get ('amount')
    self.currency = request.json.get ('currency')
