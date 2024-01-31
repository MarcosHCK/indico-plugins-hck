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
from indico_payment_enzona import _
from indico_payment_enzona.blueprint import blueprint
from indico.core.plugins import IndicoPlugin, url_for_plugin
from indico.modules.events.payment import PaymentEventSettingsFormBase
from indico.modules.events.payment import PaymentPluginMixin
from indico.modules.events.payment import PaymentPluginSettingsFormBase
from indico.modules.events.payment.views import WPPaymentEvent
from wtforms.fields import IntegerField, StringField, URLField
from wtforms.validators import DataRequired, Optional

class PluginSettingsForm (PaymentPluginSettingsFormBase):
  url = URLField (_("API Url"), [DataRequired ()], description = _('Enzona REST API Url.'))
  api_token = StringField (_("API Token"), [DataRequired ()], description = _("Enzona REST API Token"))
  merchant_id = StringField (_("Merchant ID"), [DataRequired ()], description = _("Enzona merchant identifier"))
  user_name = StringField (_('User name'), [DataRequired ()], description = _('Enzona merchant user name'))
  valid_time = IntegerField (_('Valid time'), [DataRequired ()], description = _('Payment valid time (0 for everlasting payments)'))

class EventSettingsForm (PaymentEventSettingsFormBase):

  pass

class EnzonaPaymentPlugin (PaymentPluginMixin, IndicoPlugin):
  """Enzona

  Provides a payment method using the Enzona API.
  """

  configurable = True
  settings_form = PluginSettingsForm
  event_settings_form = EventSettingsForm

  default_settings = { 'method_name' : 'Enzona', 'api_token' : '', 'merchant_id' : '', 'url' : '', 'user_name' : '', 'valid_time' : 0, }
  default_event_settings = { 'enabled' : False, 'method_name' : None, }

  def adjust_payment_form_data (self, data):

    registration = data ['registration']
    data ['cancel_url'] = url_for_plugin ('payment_enzona.cancel', registration.locator.uuid, _external = True)
    data ['proceed_url'] = url_for_plugin ('payment_enzona.proceed', registration.locator.uuid, _external = True)
    data ['status_url'] = url_for_plugin ('payment_enzona.status', registration.locator.uuid, _external = True)

  def get_blueprints (self):
    return blueprint

  def init (self):
    super ().init ()
    self.inject_bundle ('payment.js', WPPaymentEvent)

  @property
  def logo_url (self):
    return url_for_plugin ('payment_enzona.static', filename = 'images/logo.png')
