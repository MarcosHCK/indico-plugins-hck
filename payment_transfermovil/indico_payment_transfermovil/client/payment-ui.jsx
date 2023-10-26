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
import {Grid} from 'semantic-ui-react'
import {Image} from 'semantic-ui-react'
import {makeAsyncDebounce} from 'indico/utils/debounce'
import {Modal} from 'semantic-ui-react'
import {sprintf} from 'sprintf-js/src/sprintf'
import {Translate} from './i18n'
import PropTypes from 'prop-types'
import React from 'react'
import ReactDOM from 'react-dom'

const $t = $T.domain ('payment_transfermovil')

export function spawnQrButton ({ amount, cancel_url, csrf_token, currency, proceed_url, status_url, validTime, }, container)
{
  const doFetch = (url, data, silent = false) =>
    new Promise ((resolve, reject) =>
      $.ajax (
    {
      cache : false,
      complete : silent ? () => {} : IndicoUI.Dialogs.Util.progress (),
      data : JSON.stringify ($.extend ({}, data || {})),
      dataType : 'json',
      error : (error) => handleAjaxError (error) && reject (error),
      headers : { 'Content-Type' : 'application/json', 'X-CSRF-Token' : csrf_token, },
      success: (data) => handleAjaxError (data) ? reject (error) : resolve (data),
      type : 'POST',
      url : url,
    }))

  const checkTimer = makeAsyncDebounce (4000)

  const onCancel = async () =>
    {
      checkTimer (() => {})

      await doFetch (cancel_url)
      location.reload ()
    }

  const onCheck = async (manual) =>
    {
      const json = await doFetch (status_url, {}, manual == false)

      if (json.status == 'successful')
        location.reload ()
      else if (json.status != 'pending')
        throw new Error ('Unknown payment state \'' + json.status + '\'')
      else if (json.status == 'pending' && manual)
        {
          const divTag = document.createElement ('div')
          const onClose = () => document.body.removeChild (divTag)

          const widget =
            <Modal defaultOpen={true} closeIcon onClose={onClose} size={'mini'}>
              <Modal.Content>
                <p><Translate>Pending payment, check again later</Translate></p>
              </Modal.Content>
            </Modal>

          ReactDOM.render (widget, divTag)
          document.body.appendChild (divTag)
        }
    }

  const onQuery = async () =>
    {
      const data = { amount : amount, currency : currency, }
      const json = await doFetch (proceed_url, data)

      const divTag = document.createElement ('div')
      const autoCheck = () => { onCheck (false); checkTimer (autoCheck) }
      const manualCheck = () => onCheck (true)

      checkTimer (autoCheck)

      ReactDOM.render (<QrDialog onCancel={onCancel} onCheck={manualCheck} qrData={json.qr} validTime={validTime} />, divTag)
      document.body.appendChild (divTag)
    }

  ReactDOM.render (<QrButton onQuery={onQuery} />, container)
}

export class QrButton extends React.Component
{
  constructor (props)
    {
      super (props)
      this.state = { disabled : false, }
    }

  static propTypes = { onQuery : PropTypes.func.isRequired, }

  render ()
    {
      return (
        <Button onClick={this.props.onQuery} disabled={this.state.disabled}>
          <Translate>Query QR</Translate>
        </Button>)
    }
}

export class TimerWidget extends React.Component
{
  constructor (props)
    {
      super (props)
      this.topTime = this.props.timeout + new Date ().getTime ()
      this.state = { time : new Date ().getTime (), }
    }

  static propTypes =
    {
      /* in milliseconds */
      timeout : PropTypes.number.isRequired,
    }

  componentDidMount ()
    {
      this.timerID = setInterval (() => this.setState ({ time : new Date ().getTime (), }), 1000)
    }

  componentWillUnmount ()
    {
      clearInterval (this.timerID)
    }

  render ()
    {
      if (this.topTime < this.state.time)

        return <p><Translate>Timeout!</Translate></p>
      else
        {
          const time = this.topTime - this.state.time
          const seconds = ((time / 1000)|0) % 60
          const minutes = ((time / 60000)|0) % 60
          const hours = ((time / 3600000)|0) % 60

          if (hours == 0)
            return <p>{ sprintf ('%02u:%02u', minutes, seconds) }</p>
          else
            return <p>{ sprintf ('%02u:%02u:%02u', hours, minutes, seconds) }</p>
        }
    }
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

      /* In seconds */
      validTime : PropTypes.number.isRequired,
    }

  handleCancel = (event) => _.invoke (this.props, 'onCancel', event)
  handleCheck = (event) => _.invoke (this.props, 'onCheck', event)

  render ()
    {
      return (
        <Modal closeOnDimmerClick={false} closeOnEscape={false} defaultOpen={true} size={'mini'}>

          <Modal.Content>
            <p><Translate>Scan the QR code to complete the payment</Translate></p>
          </Modal.Content>

          <Modal.Content>
            <Image centered src={ 'data:image/svg+xml;base64,' + this.props.qrData } />
          </Modal.Content>

          <Modal.Content>
            <p>
              <Translate>Click</Translate> <a onClick={this.handleCheck}>
              <Translate>here</Translate>
         </a> <Translate>if the payment is not completed automatically</Translate>
            </p>
          </Modal.Content>

          <Modal.Actions>
            <Grid columns='equal'>
              <Grid.Column floated='left'>
                <TimerWidget timeout={this.props.validTime * 1000} />
              </Grid.Column>
              <Grid.Column floated='right'>
                <Button onClick={this.handleCancel}>
                  <Translate>Cancel</Translate>
                </Button>
              </Grid.Column>
            </Grid>
          </Modal.Actions>
        </Modal>)
    }
}
