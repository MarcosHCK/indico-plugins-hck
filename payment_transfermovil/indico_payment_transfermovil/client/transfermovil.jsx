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
import _ from 'lodash'
import {Button} from 'semantic-ui-react'
import {Image} from 'semantic-ui-react'
import {Modal} from 'semantic-ui-react'
import {Translate} from './i18n'
import PropTypes from 'prop-types'
import React from 'react'

const $t = $T.domain ('payment_transfermovil')

export class QrDialog extends React.Component
{
  static defaultProps =
    {
      onCancel : (event) => console.log ('missing onCancel handler'),
    }

  static propTypes =
    {
      onCancel : PropTypes.func,
      qrData : PropTypes.string.isRequired,
    }

  handleCancel = (event) => _.invoke (this.props, 'onCancel', event)

  render ()
    {
      return (
        <Modal closeOnDimmerClick={false} closeOnEscape={false} defaultOpen={true} size={'mini'}>
          <Modal.Content>
            <p><Translate>Scan the QR code to complete the payment</Translate></p>
            <Image centered src={ 'data:image/svg+xml;base64,' + this.props.qrData } />
            <p><Translate>Click here if the payment is not completed automatically</Translate></p>
          </Modal.Content>

          <Modal.Actions>
            <Button onClick={this.handleCancel}>
              <Translate>Cancel</Translate>
            </Button>
          </Modal.Actions>
        </Modal>)
    }
}
