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
from flask_pluginengine import current_plugin
from indico_payment_transfermovil import _
from indico_payment_transfermovil.blueprint import blueprint
from indico.core.plugins import IndicoPlugin, url_for_plugin
from indico.modules.events.payment import PaymentEventSettingsFormBase
from indico.modules.events.payment import PaymentPluginMixin
from indico.modules.events.payment import PaymentPluginSettingsFormBase
from indico.modules.events.payment.views import WPPaymentEvent
from indico.modules.events.payment.views import WPPaymentEventManagement
from indico.util.string import remove_accents, str_to_ascii
from wtforms.fields import IntegerField, StringField, URLField
from wtforms.validators import DataRequired, Optional

class PluginSettingsForm (PaymentPluginSettingsFormBase):
  url = URLField (_("API URL"), [DataRequired ()], description = _('URL of the Transfermovil REST API.'))
  phone_number = StringField (_('Phone number'), [DataRequired ()], description = _('Phone number associated with the bank account'))
  source_id = IntegerField (_('Service identifier'), [DataRequired ()], description = _('Transfermovil service identifier'))
  user_name = StringField (_('Service user name'), [DataRequired ()], description = _('Transfermovil service user name'))
  valid_time = IntegerField (_('Payment valid time'), [DataRequired ()], description = _('Payment valid time (in seconds)'))

class EventSettingsForm (PaymentEventSettingsFormBase):
  phone_number = StringField (_('Phone number'), [Optional ()], description = _('Phone number associated with the bank account'))

class TransfermovilPaymentPlugin (PaymentPluginMixin, IndicoPlugin):
  """Transfermovil

  Provides a payment method using the Transfermovil API.
  """

  configurable = True
  settings_form = PluginSettingsForm
  event_settings_form = EventSettingsForm

  default_settings = { 'method_name' : 'Transfermovil', 'phone_number' : '', 'source_id' : 0, 'user_name' : '', 'url' : '', 'valid_time' : 600, }
  default_event_settings = { 'enabled' : False, 'method_name' : None, 'phone_number' : None, }

  def adjust_payment_form_data (self, data):
    registration = data ['registration']
    data ['cancel_url'] = url_for_plugin ('payment_transfermovil.cancel', registration.locator.uuid, _external = True)
    data ['proceed_url'] = url_for_plugin ('payment_transfermovil.proceed', registration.locator.uuid, _external = True)
    data ['status_url'] = url_for_plugin ('payment_transfermovil.status', registration.locator.uuid, _external = True)
    data ['valid_time'] = current_plugin.settings.get ('valid_time')

  def get_blueprints (self):
     return blueprint

  def init (self):
    super ().init ()
    self.inject_bundle ('payment.js', WPPaymentEvent)

  @property
  def logo_url (self):
    return url_for_plugin ('payment_transfermovil.static', filename = 'images/logo.png')
