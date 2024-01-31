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
from io import BytesIO
from os import urandom
from qrcode.image import svg
import qrcode

def check_secret (seed: str, salt: bytes, secret: bytes) -> bool:

  seed = seed.encode ('utf-8')
  algo = PBKDF2HMAC (algorithm = hashes.SHA256 (), length = 128, salt = salt, iterations = 480000)

  try:
    # Why in the hell this method should raise an
    # exception if the keys are different?
    # Exception are exceptional, like a I/O error,
    # not a return value for God's sake.
    algo.verify (seed, secret)
    return True

  except InvalidKey:

    return False

def deserialize_secret (secret: str) -> bytes:

  return b64decode (secret.encode ('utf-8'))

def generate_qr (data: str) -> str:
  stream = BytesIO ()
  generator = qrcode.make (data, image_factory = qrcode.image.svg.SvgPathImage)
  generator.save (stream)
  result = b64encode (stream.getvalue ()).decode ()
  return result

def make_external_id (uuid: str) -> str:
  return f'Indico{{{uuid}}}'

def make_salt () -> bytes:

  return urandom (16)

def make_secret (seed: str, salt: bytes) -> bytes:

  seed = seed.encode ('utf-8')
  algo = PBKDF2HMAC (algorithm = hashes.SHA256 (), length = 128, salt = salt, iterations = 480000)
  return algo.derive (seed)

def serialize_secret (secret: bytes) -> str:

  return b64encode (secret).decode ('utf-8')
