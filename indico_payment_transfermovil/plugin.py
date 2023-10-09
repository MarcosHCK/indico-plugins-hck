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
from indico_payment_transfermovil import _
from indico_payment_transfermovil.blueprint import blueprint
from indico.core.plugins import IndicoPlugin, url_for_plugin
from indico.modules.events.payment import (PaymentEventSettingsFormBase, PaymentPluginMixin, PaymentPluginSettingsFormBase)
from indico.util.string import remove_accents, str_to_ascii
from wtforms.fields import IntegerField, StringField, URLField
from wtforms.validators import DataRequired, Optional

class PluginSettingsForm (PaymentPluginSettingsFormBase):
  url = URLField (_("API URL"), [DataRequired ()], description = _('URL of the Transfermovil REST API.'))
  user_name = StringField (_('Service user name'), [DataRequired ()], description = _('Transfermovil service user name'))
  source_id = IntegerField (_('Service identifier'), [DataRequired ()], description = _('Transfermovil service identifier'))

class EventSettingsForm (PaymentEventSettingsFormBase):
  user_name = StringField (_('Service user name'), [Optional ()], description = _('Transfermovil service user name'))
  source_id = IntegerField (_('Service identifier'), [Optional ()], description = _('Transfermovil service identifier'))

class TransfermovilPaymentPlugin (PaymentPluginMixin, IndicoPlugin):
  """Transfermovil

  Provides a payment method using the Transfermovil API.
  """

  configurable = True
  settings_form = PluginSettingsForm
  event_settings_form = EventSettingsForm

  default_settings = { 'method_name' : 'Transfermovil', 'source_id' : '', 'user_name' : '', 'url' : '', }
  default_event_settings = { 'enabled' : False, 'method_name' : None, 'source_id' : None, 'user_name' : None, }

  def adjust_payment_form_data (self, data):
    registration = data ['registration']
    data ['cancel_url'] = url_for_plugin ('payment_transfermovil.cancel', registration.locator.uuid, _external = True)
    data ['notify_url'] = url_for_plugin ('payment_transfermovil.notify', registration.locator.uuid, _external = True)
    data ['proceed_url'] = url_for_plugin ('payment_transfermovil.proceed', registration.locator.uuid, _external = True)

  def get_blueprints (self):
     return blueprint

  def init (self):
    super ().init ()
