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
from flask_pluginengine import render_plugin_template
from indico.modules.events.registration.models.registrations import Registration
from indico.web.flask.util import NotFound
from indico.web.rh import RH
from werkzeug.exceptions import BadRequest

class RHTransfermovil (RH):

  CSRF_ENABLED = False

  def _process_args (self):
    self.token = request.args ['token']
    self.registration = Registration.query.filter_by (uuid = self.token).first ()

    if not self.registration:
      raise BadRequest


class RHTransfermovilNotify (RHTransfermovil):

  def _process (self):
    NotFound ()

class RHTransfermovilProceed (RHTransfermovil):

  def _process (self):
    NotFound ()
