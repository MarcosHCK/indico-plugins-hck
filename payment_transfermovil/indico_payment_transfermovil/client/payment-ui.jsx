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
import 'jquery'
import {Button} from 'semantic-ui-react'
import {Image} from 'semantic-ui-react'
import {Modal} from 'semantic-ui-react'
import {Translate} from './i18n'
import PropTypes from 'prop-types'
import React from 'react'
import ReactDOM from 'react-dom'

const $t = $T.domain ('payment_transfermovil')

export function spawnQrButton ({ amount, cancel_url, csrf_token, currency, proceed_url, status_url, }, container)
{
  const _dialog = (qrData, onCancel, onCheck) => <QrDialog onCancel={onCancel} onCheck={onCheck} qrData={qrData} />
  const _button = (onClick) => <Button onClick={onClick}><Translate>Query QR</Translate></Button>

  const _fetch = (url, data) =>
    new Promise ((resolve, reject) =>
      $.ajax (
        {
          cache : false,
          complete : IndicoUI.Dialogs.Util.progress (),
          data : JSON.stringify ($.extend ({}, data || {})),
          dataType : 'json',
          error : (error) => handleAjaxError (error) && reject (error),
          headers : { 'Content-Type' : 'application/json', 'X-CSRF-Token' : csrf_token, },
          success: (data) => handleAjaxError (data) ? reject (error) : resolve (data),
          type : 'POST',
          url : url,
        }))

  const _cancel = () =>
    {
      _fetch (cancel_url)
      .then (() =>
        {
          location.reload ()
        })
    }

  const _check = (manual) =>
    {
      _fetch (status_url)
      .then ((json) =>
        {
          if (json.status == 'successful')
            location.reload ()
          else if (json.status == 'pending' && manual)
            {
              const divTag = document.createElement ('div')
              const onClose = () => document.body.removeChild (divTag)

              const dialog =
                <Modal defaultOpen={true} closeIcon onClose={onClose} size={'mini'}>
                  <Modal.Content>
                    <p><Translate>Pending payment, check again later</Translate></p>
                  </Modal.Content>
                </Modal>

              ReactDOM.render (dialog, divTag)
              document.body.appendChild (divTag)
            }
          else if (json.status != 'pending')
            {
              throw new Error ('Unknown payment state ' + json.status)
            }
        })
    }

  const _query = () =>
    {
      _fetch (proceed_url, { amount : amount, currency : currency, })
      .then ((json) =>
        {
          const check = () => _check (true)
          const dialog = _dialog (json.qr, _cancel, check)
          const divTag = document.createElement ('div')

          ReactDOM.render (dialog, divTag)
          document.body.appendChild (divTag)
        })
    }

  ReactDOM.render (_button (_query), container)
}

export class QrDialog extends React.Component
{
  static defaultProps =
    {
      onCancel : (event) => console.log ('missing onCancel handler') && false,
      onCheck : (event) => console.log ('missing onCheck handler') && false,
    }

  static propTypes =
    {
      defaultOpen : PropTypes.bool,
      onCancel : PropTypes.func,
      onCheck : PropTypes.func,
      qrData : PropTypes.string.isRequired,
    }

  handleCancel = (event) => _.invoke (this.props, 'onCancel', event)
  handleCheck = (event) => _.invoke (this.props, 'onCheck', event)

  render ()
    {
      return (
        <Modal closeOnDimmerClick={false} closeOnEscape={false} defaultOpen={true} size={'mini'}>
          <Modal.Content>
            <p>
              <Translate>Scan the QR code to complete the payment</Translate>
            </p>

            <Image centered src={ 'data:image/svg+xml;base64,' + this.props.qrData } />

            <p>
              <Translate>Click</Translate> <a onClick={this.handleCheck}>
              <Translate>here</Translate>
         </a> <Translate>if the payment is not completed automatically</Translate>
            </p>
          </Modal.Content>

          <Modal.Actions>
            <Button onClick={this.handleCancel}>
              <Translate>Cancel</Translate>
            </Button>
          </Modal.Actions>
        </Modal>)
    }
}
