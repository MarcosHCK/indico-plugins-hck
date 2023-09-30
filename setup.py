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

from setuptools import setup, find_packages

setup(
    name='indico_payment_transfermovil',
    version='0.0.1',
    packages=find_packages (),
    zip_safe=False,
    include_package_data=True,
    install_requires=['indico>=3.0'],
    entry_points={'indico.plugins': {'payment_transfermovil = indico_payment_transfermovil:PaymentTransfermovil'}}
)
