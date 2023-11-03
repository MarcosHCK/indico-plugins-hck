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
from base64 import b64decode, b64encode
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from flask_pluginengine import current_plugin
from indico.modules.events.registration.models.registrations import Registration
from io import BytesIO
from os import urandom
from qrcode.image import svg
import qrcode

def check_nonce (password : bytes, salt : bytes, nonce : bytes) -> bool:
  algo = PBKDF2HMAC (algorithm = hashes.SHA256 (), length = 128, salt = salt, iterations = 480000)

  try:
    # Why in the hell this method should raise an
    # exception if the keys are different?
    # Exception are exceptional, like a I/O error,
    # not a return value for God's sake.
    algo.verify (password, nonce)
    return True
  except InvalidKey:
    return False

def deserialize_password (password : str) -> bytes:
  return b64decode (password.encode ('utf-8'))

def genereate_nonce (password : bytes, salt : bytes) -> bytes:
  return PBKDF2HMAC (algorithm = hashes.SHA256 (), length = 128, salt = salt, iterations = 480000).derive (password)
  
def genereate_salt () -> bytes:
  return urandom (16)

def genereate_qr (data : str) -> str:

  stream = BytesIO ()
  generator = qrcode.make (data, image_factory = qrcode.image.svg.SvgPathImage)
  generator.save (stream)
  result = b64encode (stream.getvalue ()).decode ()
  return result


def get_phone_number (registration : Registration) -> str:
  event = registration.registration_form.event
  event_settings = current_plugin.event_settings
  settings = current_plugin.settings

  if (not event_settings.get (event, 'phone_number')):
    return settings.get ('phone_number')
  else:
    return event_settings.get (event, 'phone_number')

def make_external_id (uuid : str) -> str:
  return f'Indico{{{uuid}}}'

def make_password (uuid : str) -> str:
  sourceid = current_plugin.settings.get ('source_id')
  username = current_plugin.settings.get ('user_name')
  password = f'{username}-{sourceid}-{uuid}'
  return password.encode ('utf-8')

def serialize_password (password : bytes) -> str:
  return b64encode (password).decode ('utf-8')
