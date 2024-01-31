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
import 'indico/jquery/utils/errors'
import 'jquery'
import { Button } from 'semantic-ui-react'
import { makeAsyncDebounce } from 'indico/utils/debounce'
import { Modal } from 'semantic-ui-react'
import { QrDialog } from './QrDialog'
import { Translate } from './i18n'
import React, { useState } from 'react'
import ReactDOM from 'react-dom'

export function spawnQrButton (args, container)
{
  const checkTimer = makeAsyncDebounce (4000)
  const { amount, cancel_url, csrf_token, currency, proceed_url, status_url, validTime, } = args

  const doFetch = (url, data = {}, silent = false) => new Promise ((resolve, reject) => $.ajax (
    {
      cache : false,
      complete : silent ? () => {} : IndicoUI.Dialogs.Util.progress (),
      data : JSON.stringify ($.extend ({}, data || {})),
      dataType : 'json',
      error : (error) => handleAjaxError (error) && reject (error),
      headers : { 'Content-Type' : 'application/json', 'X-CSRF-Token' : csrf_token, },
      success: (data) => handleAjaxError (data) ? reject (data) : resolve (data),
      type : 'POST',
      url : url,
    }))

  const onCancel = async () => { checkTimer (() => {}); await doFetch (cancel_url); location.reload () }

  const onCheck = async (manual) =>
    {
      const json = await doFetch (status_url, {}, manual == false)

      if (json.status == 'successful')
        location.href = json.redirect_url
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

  const onQueryQr = async () =>
    {
      const json = await doFetch (proceed_url, { amount : amount, currency : currency, method : 'qr', })

      const divTag = document.createElement ('div')
      const autoCheck = () => { onCheck (false); checkTimer (autoCheck) }
      const manualCheck = () => onCheck (true)

      ReactDOM.render (<QrDialog onCancel={onCancel} onCheck={manualCheck} qrData={json.qr} validTime={validTime} />, divTag)
      document.body.appendChild (divTag)
      checkTimer (autoCheck)
    }

  const onQueryUrl = async () =>
    {

      const waiter = IndicoUI.Dialogs.Util.progress ()

      try
        {
          const json = await doFetch (proceed_url, { amount : amount, currency : currency, method : 'url', }, true)
          location.href = json.redirect_url
        }
      catch (e) { waiter () }
    }

  ReactDOM.render (
    <>
      <Button onClick={() => onQueryQr ()}>
        <Translate>Pay with QR</Translate>
      </Button>
      <Button onClick={() => onQueryUrl ()}>
        <Translate>Pay</Translate>
      </Button>
    </>, container)
}
