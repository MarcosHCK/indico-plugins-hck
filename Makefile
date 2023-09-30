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

default all: pack transfer

pack: setup.py $(shell find indico_payment_transfermovil -type f -name "*.py")
	python setup.py sdist

transfer: pack
	pip install ./dist/indico_payment_transfermovil-0.0.1.tar.gz
