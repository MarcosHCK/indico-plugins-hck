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
from indico.core.plugins import IndicoPluginBlueprint
from indico_payment_transfermovil.controllers import RHTransfermovilCancel
from indico_payment_transfermovil.controllers import RHTransfermovilNotify
from indico_payment_transfermovil.controllers import RHTransfermovilProceed

blueprint = IndicoPluginBlueprint (
  'payment_transfermovil', __name__,
  url_prefix = '/event/<int:event_id>/registrations/<int:reg_form_id>/payment/response/transfermovil'
    )

blueprint.add_url_rule ('/cancel', 'cancel', RHTransfermovilCancel, methods = ('POST',))
blueprint.add_url_rule ('/notify', 'notify', RHTransfermovilNotify, methods = ('POST',))
blueprint.add_url_rule ('/proceed', 'proceed', RHTransfermovilProceed, methods = ('POST',))
