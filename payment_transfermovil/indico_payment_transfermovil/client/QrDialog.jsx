/* Copyright (c) 2023-2025 MarcosHCK
 * This file is part of indico-plugins-hck.
 *
 * indico-plugins-hck is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * indico-plugins-hck is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with indico-plugins-hck. If not, see <http://www.gnu.org/licenses/>.
 */
import { Button } from 'semantic-ui-react'
import { Grid } from 'semantic-ui-react'
import { Image } from 'semantic-ui-react'
import { Modal } from 'semantic-ui-react'
import { Translate } from './i18n'
import { TimerWidget } from './TimerWidget'
import React from 'react'

export function QrDialog (props)
{
  const { onCancel, onCheck, qrData, validTime } = props

  return (
    <Modal closeOnDimmerClick={false} closeOnEscape={false} defaultOpen={true} size='mini'>

      <Modal.Content>
        <p>
          <Translate>Scan the QR code to complete the payment</Translate>
        </p>
      </Modal.Content>

      <Modal.Content>
        <Image alt='qr code' centered src={ 'data:image/svg+xml;base64,' + qrData } />
      </Modal.Content>

      <Modal.Content>
        <p>
          <Translate>Click</Translate> <a onClick={() => onCheck ()}>
            <Translate>here</Translate>
          </a> <Translate>if the payment is not completed automatically</Translate>
        </p>
      </Modal.Content>

      <Modal.Actions>
        <Grid columns='equal'>
          <Grid.Column floated='left'>
            <TimerWidget time={validTime * 1000} />
          </Grid.Column>
          <Grid.Column floated='right'>
            <Button onClick={() => onCancel ()}>
              <Translate>Cancel</Translate>
            </Button>
          </Grid.Column>
        </Grid>
      </Modal.Actions>
    </Modal>)
}
