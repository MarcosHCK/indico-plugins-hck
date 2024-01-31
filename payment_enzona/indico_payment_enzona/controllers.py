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
from enzona_transfermovil import PermiteCrearUnPagoApi
from enzona_transfermovil.models.payments_post_request import PaymentsPostRequest
from enzona_transfermovil.models.payments_post_request_items_inner import PaymentsPostRequestItemsInner
from enzona_transfermovil.models.payments_post200_response import PaymentsPost200Response
from flask import request
from flask_pluginengine import url_for_plugin
from indico_payment_enzona.rh import RHEnzonaWithoutTransaction
from indico_payment_enzona.rh import RHEnzonaWithTransaction
from indico_payment_enzona.utils import check_secret
from indico_payment_enzona.utils import deserialize_secret
from indico_payment_enzona.utils import generate_qr
from indico_payment_enzona.utils import make_external_id
from indico_payment_enzona.utils import make_salt
from indico_payment_enzona.utils import make_secret
from indico_payment_enzona.utils import serialize_secret
from werkzeug.exceptions import InternalServerError

class RHEnzonaCancel (RHEnzonaWithTransaction):

  def _process (self):

    if (not self._has_transaction ()):
      current_plugin.logger.info ("Payment not recorded because transaction was not valid")
      raise BadRequest ()
    else:

      externalid = make_external_id (self.token)

      if (request.args.get ('secret') == None):

        current_plugin.logger.info ('Payment not recorded because transaction did not sent a valid password header field')
        raise BadRequest ()

      salt = deserialize_secret (transaction.data ['salt'])
      secret = deserialize_secret (request.args.get ('secret'))

      if (not check_secret (externalid, salt, secret)):

        current_plugin.logger.info ('Payment not recorded because transaction password is invalid')
        raise BadRequest ()

      self._register (TransactionAction.reject, {})
      return { "Success" : True, "Resultmsg" : "OK", "Status" : 1, }

class RHEnzonaNotify (RHEnzonaWithTransaction):

  def _process (self):

    if (not self._has_transaction ()):
      current_plugin.logger.info ('Payment not recorded because there where no transaction')
      raise BadRequest ()
    else:

      externalid = make_external_id (self.token)

      if (request.args.get ('secret') == None):

        current_plugin.logger.info ('Payment not recorded because transaction did not sent a valid password header field')
        raise BadRequest ()

      salt = deserialize_secret (transaction.data ['salt'])
      secret = deserialize_secret (request.args.get ('secret'))

      if (not check_secret (externalid, salt, secret)):

        current_plugin.logger.info ('Payment not recorded because transaction password is invalid')
        raise BadRequest ()

      self._register (TransactionAction.complete, transaction.data)
      return { "Success" : True, "Resultmsg" : "OK", "Status" : 1, }

class RHEnzonaProceed (RHEnzonaWithoutTransaction):

  CSRF_ENABLED = True

  def _process ():

    if (not self._has_not_transaction ()):
      current_plugin.logger.info ('Payment not recorded because transaction was not valid')
      raise BadRequest ()
    else:

      if (request.args ['method'] == 'qr'):

        raise Exception ('unimplemented')
      else:

        api_token = current_plugin.settings.get ('api_token')
        externalid = make_external_id (self.token)
        merchant_id = current_plugin.settings.get ('merchant_id')
        password = make_password (self.token)
        user_name = current_plugin.settings.get ('user_name')
        valid_time = current_plugin.settings.get ('valid_time')

        salt = make_salt ()
        secret = make_secret (externalid, salt)

        cancel_url = url_for_plugin ('payment_transfermovil.cancel', self.registration.locator.uuid, secret = serialize_secretdeserialize_secret (secret), _external = True)
        notify_url = url_for_plugin ('payment_transfermovil.notify', self.registration.locator.uuid, secret = serialize_secretdeserialize_secret (secret), _external = True)

        payload = PaymentsPostRequest ()
        item = PaymentsPostRequestItemsInner ()

        item.description = 'Indico Event Payment'
        item.name = 'Indico Event Payment'
        item.price = self.amount
        item.quantity = 1
        item.tax = 0

        payload.amount = self.amount
        payload.cancel_url = cancel_url
        payload.currency = self.currency
        payload.description = 'Indico Event Payment'
        payload.invoice_number = ''
        payload.items = [item]
        payload.merchant_op_id = externalid
        payload.merchant_uuid = merchant_id
        payload.return_url = notify_url
        payload.terminal_id = ''
        payload.username = user_name
        payload.valid_time = valid_time

        try:
          headers = { 'Authorize' : f'Bearer {api_token}' }
          request = PermiteCrearUnPagoApi ()

          response = request.payments_post (payload, headers = headers, _request_auth = 'OAuth2')

        except Exception as e:

          current_plugin.logger.warning (f'Transfermovil API request exception: {e}')
          raise InternalServerError ()

        options = \
          {
            'created_at' : response.created_at,
            'transaction_uuid' : response.transaction_uuid,
            'salt' : serialize_secretdeserialize_secret (salt),
            'update_at' : response.update_at,
          }

        if (not response.links):

          raise InternalServerError ()
        else:

          for link in response.links:

            if (str.lower (link.rel) == 'confirm' and str.lower (link.method) == 'redirect'):

              self._register (TransactionAction.pending, options)
              return { 'redirect' : True, 'redirect_url' : link.href }

        raise InternalServerError ()

class RHEnzonaStatus (RHEnzonaWithTransaction):

  CSRF_ENABLED = True

  def _process ():

    transaction = self.registration.transaction

    if (not transaction):
      current_plugin.logger.info ("Payment not recorded because transaction was not valid")
      raise BadRequest ()
    else:

      if (transaction.provider != 'enzona'):
        current_plugin.logger.info ("Payment not recorded because transaction was not valid")
        raise BadRequest ()
      else:

        if (transaction.status != TransactionStatus.successful):

          return { 'status' : transaction.status.name, }
        else:

          return \
            {
              'redirect' : True,
              'redirect_url' : url_for ('event_registration.display_regform', self.registration.locator.registrant),
              'status' : transaction.status.name,
            }
