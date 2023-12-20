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
from indico.modules.events.payment.models.transactions import TransactionStatus
from indico.modules.events.payment.util import register_transaction
from indico.modules.events.registration.models.registrations import Registration
from indico.web.rh import RH
from werkzeug.exceptions import BadRequest

class RHEnzona (RH):

  def _process_args (self):
    self.token = request.args ['token']
    self.registration = Registration.query.filter_by (uuid = self.token).first ()

    if (not self.registration):
      raise BadRequest ()

  def _register (self, action : str, data : str) -> None:

    register_transaction (
      action = action,
      amount = self.amount,
      currency = self.currency,
      data = data,
      provider = 'enzona',
      registration = self.registration)

class RHEnzonaWithTransaction (RHEnzona):

  def _has_transaction (self) -> bool:

    transaction = self.registration.transaction

    if (not transaction):
      return False
    else:

      provider = self.registration.transaction.provider
      status = self.registration.transaction.status
      return provider == 'enzona' and status == TransactionStatus.pending

  def _process_args (self):
    super ()._process_args ()

    if (not self.registration.transaction):
      raise BadRequest ()
    else:

      self.amount = self.registration.transaction.amount
      self.currency = self.registration.transaction.currency

class RHEnzonaWithoutTransaction (RHEnzona):

  def _has_not_transaction (self) -> bool:

    transaction = self.registration.transaction

    if (not self.registration.transaction):
      return True
    else:

      rejected = transaction.status == TransactionStatus.rejected
      cancelled = transaction.status == TransactionStatus.cancelled
      return rejected or cancelled
