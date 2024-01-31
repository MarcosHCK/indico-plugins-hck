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
from indico.core.plugins import IndicoPluginBlueprint
from indico_payment_enzona.controllers import RHEnzonaCancel
from indico_payment_enzona.controllers import RHEnzonaNotify
from indico_payment_enzona.controllers import RHEnzonaProceed
from indico_payment_enzona.controllers import RHEnzonaStatus

blueprint = IndicoPluginBlueprint (
  'payment_enzona', __name__,
  url_prefix = '/event/<int:event_id>/registrations/<int:reg_form_id>/payment/enzona'
    )

blueprint.add_url_rule ('/cancel', 'cancel', RHEnzonaCancel, methods = ('POST',))
blueprint.add_url_rule ('/notify', 'notify', RHEnzonaNotify, methods = ('POST',))
blueprint.add_url_rule ('/proceed', 'proceed', RHEnzonaProceed, methods = ('POST',))
blueprint.add_url_rule ('/status', 'status', RHEnzonaStatus, methods = ('GET',))
