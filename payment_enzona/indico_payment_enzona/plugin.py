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
from wtforms.fields import StringField, URLField
from wtforms.validators import DataRequired, Optional

class PluginSettingsForm (PaymentPluginSettingsFormBase):
  url = URLField (_("API Url"), [DataRequired ()], description = _('Enzona REST API Url.'))
  token = StringField (_("API Token"), [DataRequired ()], description = _("Enzona REST API Token"))
  phone_number = StringField (_('Phone number'), [DataRequired ()], description = _('Phone number associated with the bank account'))

class EventSettingsForm (PaymentEventSettingsFormBase):
  phone_number = StringField (_('Phone number'), [Optional ()], description = _('Phone number associated with the bank account'))

class EnzonaPaymentPlugin (PaymentPluginMixin, IndicoPlugin):
  """Enzona

  Provides a payment method using the Enzona API.
  """

  configurable = True
  settings_form = PluginSettingsForm
  event_settings_form = EventSettingsForm

  default_settings = { 'method_name' : 'Enzona', 'phone_number' : '', 'url' : '', }
  default_event_settings = { 'enabled' : False, 'method_name' : None, 'phone_number' : None, }

  def get_blueprints (self):
    return blueprint

  def init (self):
    super ().init ()

  @property
  def logo_url (self):
    return url_for_plugin ('payment_enzona.static', filename = 'images/logo.png')
