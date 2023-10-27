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

def deserialize_password (password : str) -> bytes:
  return b64decode (password.encode ('utf-8'))

def serialize_password (password : bytes) -> str:
  return b64encode (password).decode ('utf-8')
