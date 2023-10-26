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
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from flask import request
from flask_pluginengine import current_plugin
from indico.modules.events.payment.models.transactions import TransactionStatus
from indico.modules.events.payment.util import register_transaction
from indico.modules.events.registration.models.registrations import Registration
from indico.web.rh import RH
from os import urandom
from werkzeug.exceptions import BadRequest

class RHTransfermovil (RH):

  def _gen_external_id (self):
    return 'Indico{{{0}}}'.format (self.token)

  def _gen_nonce_password (self):
    sourceid = self._get_source_id ()
    username = self._get_user_name ()

    password = '{0}-{1}-{2}'.format (sourceid, username, self.token)
    return password.encode ('utf-8')

  def _gen_nonce_salt (self):
    return urandom (16)

  def _get_phone_number (self):
    event_settings = current_plugin.event_settings
    regform = self.registration.registration_form
    settings = current_plugin.settings

    if (not event_settings.get (regform.event, 'phone_number')):
      return settings.get ('phone_number')
    else:
      return event_settings.get (regform.event, 'phone_number')

  def _get_source_id (self):
    event_settings = current_plugin.event_settings
    regform = self.registration.registration_form
    settings = current_plugin.settings

    if (not event_settings.get (regform.event, 'source_id')):
      return settings.get ('source_id')
    else:
      return event_settings.get (regform.event, 'source_id')

  def _get_url (self):
    return current_plugin.settings.get ('url')

  def _get_user_name (self):
    event_settings = current_plugin.event_settings
    regform = self.registration.registration_form
    settings = current_plugin.settings

    if (not event_settings.get (regform.event, 'user_name')):
      return settings.get ('user_name')
    else:
      return event_settings.get (regform.event, 'user_name')

  def _process_args (self):
    self.token = request.args ['token']
    self.registration = Registration.query.filter_by (uuid = self.token).first ()

    if (not self.registration):
      raise BadRequest ()

  def _register (self, action, data):

    register_transaction (
      action = action,
      amount = self.amount,
      currency = self.currency,
      data = data,
      provider = 'transfermovil',
      registration = self.registration)

class RHTransfermovilWithTransaction (RHTransfermovil):

  def _check_nonce (self, salt, nonce):
    pswd = self._gen_nonce_password ()
    algo = PBKDF2HMAC (algorithm = hashes.SHA256 (), length = 128, salt = salt, iterations = 480000)

    try:
      # Why in the hell this method should raise an
      # exception if the keys are different?
      # Exception are exceptional, like a I/O error,
      # not a return value for God's sake.
      return algo.verify (pswd, nonce) != False
    except InvalidKey:
      return False

  def _has_transaction (self):

    transaction = self.registration.transaction

    if (not transaction):
      return False
    else:

      provider = self.registration.transaction.provider
      status = self.registration.transaction.status
      return provider == 'transfermovil' and status == TransactionStatus.pending

  def _process_args (self):
    super ()._process_args ()

    if (not self.registration.transaction):
      raise BadRequest ()
    else:

      self.amount = self.registration.transaction.amount
      self.currency = self.registration.transaction.currency

class RHTransfermovilWithoutTransaction (RHTransfermovil):

  def _gen_nonce (self, salt):
    pswd = self._gen_nonce_password ()
    algo = PBKDF2HMAC (algorithm = hashes.SHA256 (), length = 128, salt = salt, iterations = 480000)
    return algo.derive (pswd)

  def _has_not_transaction (self):

    transaction = self.registration.transaction

    if (not self.registration.transaction):
      return True
    else:
      rejected = transaction.status == TransactionStatus.rejected
      cancelled = transaction.status == TransactionStatus.cancelled
      return rejected or cancelled
