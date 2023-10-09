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
from flask import flash, redirect, request
from flask_pluginengine import current_plugin, render_plugin_template
from indico.core.plugins import url_for_plugin
from indico.modules.events.registration.models.registrations import Registration
from indico.web.flask.util import NotFound
from indico.web.rh import RH
from io import BytesIO
from qrcode.image import svg
from werkzeug.exceptions import BadRequest, InternalServerError
import base64, qrcode, requests

class RHTransfermovil (RH):

  CSRF_ENABLED = False

  def _is_duplicated (self):
    transaction = self.registration.transaction

    if (not transaction or transaction.provider != 'transfermovil'):
      return False
    return (transaction.data ['order_id'] == request.form.get ('order_id'))

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
    self.amount = request.form.get ('amount')
    self.currency = request.form.get ('currency')
    self.token = request.args ['token']

    self.registration = Registration.query.filter_by (uuid = self.token).first ()

    if not self.registration:
      raise BadRequest ()

class RHTransfermovilNotify (RHTransfermovil):

  def _process (self):

    notify = request.json

    if (self._is_duplicated ()):
      current_plugin.logger.info("Payment not recorded because transaction was duplicated\nData received: %s",
                                       request.form)
      raise BadRequest ()
    else:
      raise NotFound ()
      return { "Success" : True, "Resultmsg" : "OK", "Status" : 1, }

class RHTransfermovilProceed (RHTransfermovil):

  def _process (self):

    source_id = self._get_source_id ()

    if (self._is_duplicated ()):
      current_plugin.logger.info("Payment not recorded because transaction was duplicated\nData received: %s",
                                       request.form)
      raise BadRequest ()
    else:

      body = { "request" :
        {
          'Amount' : self.amount,
          'Currency' : self.currency,
          'Description' : "Indico Event Payment",
          'ExternalId' : self.token,
          'Source' : source_id,
          'UrlResponse' : url_for_plugin ('payment_transfermovil.notify', self.registration.locator.uuid, _external = True),
          'ValidTime' : 60 * (10),
        }}

      headers = {
          'password' : '1234',
          'source' : source_id,
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
          json = '{{ "id_transaccion" : "{id}", "importe" : {amount}, "moneda" : {currency}, "numero_proveedor" : {source_id}, "version" : 1, }}'
          json = json.format (amount = self.amount, currency = self.currency, id = response.get ('OrderId'), source_id = source_id)

          stream = BytesIO ()
          qr = qrcode.make (json, image_factory = qrcode.image.svg.SvgImage)
          qr.save (stream)

          return { "qr" : base64.b64encode (stream.getvalue ()).decode (), }
