# Copyright (c) 2023-2025 MarcosHCK
# This file is part of indico-plugins-hck.
#
# indico-plugins-hck is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# indico-plugins-hck is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with indico-plugins-hck. If not, see <http://www.gnu.org/licenses/>.
#
from flask import request
from flask_pluginengine import current_plugin
from indico_payment_transfermovil.rh import RHTransfermovilWithoutTransaction
from indico_payment_transfermovil.rh import RHTransfermovilWithTransaction
from indico_payment_transfermovil.utils import check_nonce
from indico_payment_transfermovil.utils import deserialize_password
from indico_payment_transfermovil.utils import genereate_nonce
from indico_payment_transfermovil.utils import genereate_qr
from indico_payment_transfermovil.utils import genereate_salt
from indico_payment_transfermovil.utils import get_phone_number
from indico_payment_transfermovil.utils import make_external_id
from indico_payment_transfermovil.utils import make_password
from indico_payment_transfermovil.utils import serialize_password
from indico.core.plugins import url_for_plugin
from indico.modules.events.payment.models.transactions import TransactionAction, TransactionStatus
from indico.web.flask.util import url_for
from werkzeug.exceptions import BadRequest, InternalServerError
import requests

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
      current_plugin.logger.info ('Payment not recorded because there where no transaction')
      raise BadRequest ()
    else:

      externalid = make_external_id (self.token)
      password = make_password (self.token)
      sourceid = current_plugin.settings.get ('source_id')
      username = current_plugin.settings.get ('user_name')

      if (not request.headers.get ('password')):
        current_plugin.logger.info ('Payment not recorded because transaction did not sent a valid password header field')
        raise BadRequest ()
      if (int (request.headers.get ('source')) != sourceid):
        current_plugin.logger.info ('Payment not recorded because transaction did not sent a valid source header field')
        raise BadRequest ()
      if (str (request.headers.get ('username')) != username):
        current_plugin.logger.info ('Payment not recorded because transaction did not sent a valid username header field')
        raise BadRequest ()

      try:
        notify = request.json
      except Exception:
        current_plugin.logger.info ('Payment not recorded because POST data was not valid JSON')
        raise BadRequest ()

      if (notify.get ('ExternalId') != externalid):
        current_plugin.logger.info ('Payment not recorded because transaction did not sent a valid ExternalId POST field')
        raise BadRequest ()
      if (notify.get ('Source') != sourceid):
        current_plugin.logger.info ('Payment not recorded because transaction did not sent a valid Source POST field')
        raise BadRequest ()

      transaction = self.registration.transaction

      salt = deserialize_password (transaction.data ['salt'])
      nonce = deserialize_password (request.headers.get ('password'))

      if (not check_nonce (password, salt, nonce)):
        current_plugin.logger.info ('Payment not recorded because transaction password is invalid')
        raise BadRequest ()

      data = {
          'bank_id' : notify.get ('BankId'),
          'bank' : notify.get ('Bank'),
          'order_id' : transaction.data ['order_id'],
          'phone' : notify.get ('Phone'),
          'tm_id' : notify.get ('TmId'),
        }

      self._register (TransactionAction.complete, data)
      return { 'Success' : True, 'Resultmsg' : 'OK', 'Status' : 1, }

class RHTransfermovilProceed (RHTransfermovilWithoutTransaction):

  def _process (self):

    if (not self._has_not_transaction ()):
      current_plugin.logger.info ('Payment not recorded because transaction was not valid')
      raise BadRequest ()
    else:

      externalid = make_external_id (self.token)
      password = make_password (self.token)
      phone = get_phone_number (self.registration)
      salt = genereate_salt ()
      sourceid = current_plugin.settings.get ('source_id')
      username = current_plugin.settings.get ('user_name')

      nonce = genereate_nonce (password, salt)
      result = None

      notify_url = url_for_plugin ('payment_transfermovil.notify', self.registration.locator.uuid, _external = True)

      body = {
          'request' : {
              'Amount' : self.amount,
              'Currency' : self.currency,
              'Description' : 'Indico Event Payment',
              'ExternalId' : externalid,
              'Phone' : phone,
              'Source' : sourceid,
              'UrlResponse' : notify_url,
              'ValidTime' : 60 * (10),
            }
        }

      headers = {
          'password' : serialize_password (nonce),
          'source' : str (sourceid),
          'username' : username,
        }

      try:
        result = requests.post (current_plugin.settings.get ('url'), headers = headers, json = body)
      except Exception as e:
        current_plugin.logger.warning (f'Transfermovil API request exception: {e}')
        raise InternalServerError ()

      if (not result.ok):
        current_plugin.logger.warning ('Transfermovil API request error: %i %s', result.status_code, result.reason)
        raise InternalServerError ()
      else:

        try:
          response = result.json ().get ('PayOrderResult')
        except Exception as e:
          current_plugin.logger.warning (f'Transfermovil API request response exception: {e}')
          raise InternalServerError ()

        if (response.get ('Success') != True):
          current_plugin.logger.warning ('Transfermovil API request error: failed method')
          raise InternalServerError ()
        else:

          self._register (TransactionAction.pending, { 'order_id' : response.get ('OrderId'), 'salt' : serialize_password (salt), })
          json = f'{{ "id_transaccion" : {externalid}, "importe" : {self.amount}, "moneda" : {self.currency}, "numero_proveedor" : {sourceid}, "version" : 1 }}'
          return { 'qr' : genereate_qr (json), }

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

        if (transaction.status != TransactionStatus.successful):
          return { 'status' : transaction.status.name, }
        else:
          return {
              'redirect' : True,
              'redirect_url' : url_for ('event_registration.display_regform', self.registration.locator.registrant),
              'status' : transaction.status.name, }
