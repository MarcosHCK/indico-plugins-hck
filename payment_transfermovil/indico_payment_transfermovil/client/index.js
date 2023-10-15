/* Copyright 2023 MarcosHCK
 * This file is part of PaymentTransfermovil.
 *
 * PaymentTransfermovil is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * PaymentTransfermovil is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with PaymentTransfermovil. If not, see <http://www.gnu.org/licenses/>.
 */
import { QrDialog } from './transfermovil'
import React from 'react';
import ReactDOM from 'react-dom';

import * as Transfermovil from './transfermovil'

window.showQrDialog = function (qrData, onCancel)
{
  const container = document.createElement ('div')
  const jsx = (<QrDialog onCancel={onCancel} qrData={qrData} />)

  ReactDOM.render (jsx, container)
  document.body.appendChild (container)
}

window._Transfermovil = Transfermovil
