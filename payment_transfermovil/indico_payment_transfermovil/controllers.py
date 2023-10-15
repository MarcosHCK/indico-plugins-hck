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
from flask import request
from flask_pluginengine import current_plugin
from indico_payment_transfermovil.rh import RHTransfermovilWithoutTransaction
from indico_payment_transfermovil.rh import RHTransfermovilWithTransaction
from indico_payment_transfermovil.utils import deserialize_password
from indico_payment_transfermovil.utils import serialize_password
from indico.core.plugins import url_for_plugin
from indico.modules.events.payment.models.transactions import TransactionAction, TransactionStatus
from io import BytesIO
from qrcode.image import svg
from werkzeug.exceptions import BadRequest, InternalServerError
import base64, qrcode, requests

class RHTransfermovilCancel (RHTransfermovilWithTransaction):

  CSRF_ENABLED = True

  def _process (self):

    if (not self._has_transaction ()):
      current_plugin.logger.info ("Payment not recorded because transaction was not valid")
      raise BadRequest ()
    else:

      self._register (TransactionAction.reject, {})
      return { "Success" : True, "Resultmsg" : "OK", "Status" : 1, }

class RHTransfermovilNotify (RHTransfermovilWithTransaction):

  CSRF_ENABLED = False

  def _process (self):

    if (not self._has_transaction ()):
      current_plugin.logger.info ("Payment not recorded because transaction was not valid")
      raise BadRequest ()
    else:

      if (not request.headers.get ('password')):
        current_plugin.logger.info ("Payment not recorded because transaction did not sent password header field")
        raise BadRequest ()
      if (int (request.headers.get ('source')) != self._get_source_id ()):
        current_plugin.logger.info ("Payment not recorded because transaction did not sent source header field")
        raise BadRequest ()
      if (str (request.headers.get ('username')) != self._get_user_name ()):
        current_plugin.logger.info ("Payment not recorded because transaction did not sent username header field")
        raise BadRequest ()

      notify = request.json

      if (notify.get ('ExternalId') != self._gen_external_id ()):
        current_plugin.logger.info ("Payment not recorded because transaction did not sent ExternalId POST field")
        raise BadRequest ()
      if (notify.get ('Source') != self._get_source_id ()):
        current_plugin.logger.info ("Payment not recorded because transaction did not sent Source POST field")
        raise BadRequest ()

      transaction = self.registration.transaction

      salt = deserialize_password (transaction.data ['salt'])
      nonce = deserialize_password (request.headers.get ('password'))

      if (not self._check_nonce (salt, nonce)):
        current_plugin.logger.info ("Payment not recorded because transaction password is invalid")
        print ("Payment not recorded because transaction password is invalid")
        raise BadRequest ()

      data = {
          'bank_id' : notify.get ('BankId'),
          'bank' : notify.get ('Bank'),
          'order_id' : transaction.data ['order_id'],
          'phone' : notify.get ('Phone'),
          'tm_id' : notify.get ('TmId'),
        }

      self._register (TransactionAction.complete, data)
      return { "Success" : True, "Resultmsg" : "OK", "Status" : 1, }

class RHTransfermovilProceed (RHTransfermovilWithoutTransaction):

  def _process (self):

    if (not self._has_not_transaction ()):
      current_plugin.logger.info ("Payment not recorded because transaction was not valid")
      raise BadRequest ()
    else:

      salt = self._gen_nonce_salt ()
      nonce = self._gen_nonce (salt)

      external_id = self._gen_external_id ()
      notify_url = url_for_plugin ('payment_transfermovil.notify', self.registration.locator.uuid, _external = True)

      body = {
          'request' : {
              'Amount' : self.amount,
              'Currency' : self.currency,
              'Description' : "Indico Event Payment",
              'ExternalId' : external_id,
              'Source' : self._get_source_id (),
              'UrlResponse' : notify_url,
              'ValidTime' : 60 * (10),
            }
        }

      headers = {
          'password' : serialize_password (nonce),
          'source' : str (self._get_source_id ()),
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

          self._register (TransactionAction.pending, { 'order_id' : response.get ('OrderId'), 'salt' : serialize_password (salt), })

          json = '{{ "id_transaccion" : "{id}", "importe" : {amount}, "moneda" : {currency}, "numero_proveedor" : {source_id}, "version" : 1 }}'
          json = json.format (amount = self.amount, currency = self.currency, id = external_id, source_id = self._get_source_id ())

          stream = BytesIO ()
          qr = qrcode.make (json, image_factory = qrcode.image.svg.SvgPathImage)

          qr.save (stream)

          return { "qr" : base64.b64encode (stream.getvalue ()).decode (), }

  def _process_args (self):
    super ()._process_args ()
    self.amount = request.json.get ('amount')
    self.currency = request.json.get ('currency')

class RHTransfermovilStatus (RHTransfermovilWithTransaction):

  CSRF_ENABLED = True

  def _process (self):

    transaction = self.registration.transaction

    if (not transaction):
      current_plugin.logger.info ("Payment not recorded because transaction was not valid")
      raise BadRequest ()
    else:

      if (transaction.provider != 'transfermovil'):
        current_plugin.logger.info ("Payment not recorded because transaction was not valid")
        raise BadRequest ()
      else:

        return { status : transaction.status.name, }
