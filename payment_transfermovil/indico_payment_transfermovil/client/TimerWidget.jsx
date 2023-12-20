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
import { sprintf } from 'sprintf-js'
import { Translate } from './i18n'
import React, { useEffect, useState } from 'react'

export function TimerWidget ({ time })
{
  const now = new Date ()
  const [ finalDate ] = useState (new Date (now.getTime () + time))
  const [ hasHours ] = useState (time > 3600000 + 1)
  const [ nowDate, setNowDate ] = useState (now)
  const [ timerId, setTimerId ] = useState (undefined)

  useEffect (() =>
    {
      if (typeof timerId === 'undefined')
        setTimerId (setInterval (() => setNowDate (new Date ()), 1000))
      return () =>
    {
      if (typeof timerId !== 'undefined')
    {
      clearInterval (timerId)
      setTimerId (undefined)
    }}}, [])

  if (nowDate >= finalDate)
    return <p><Translate>Timeout!</Translate></p>
  else
    {
      const finalTime = finalDate.getTime ()
      const nowTime = nowDate.getTime ()
      const time = finalTime - nowTime
      const seconds = ((time / 1000) | 0) % 60
      const minutes = ((time / 60000) | 0) % 60
      const hours = ((time / 3600000) | 0) % 60

      return hasHours == false
  ? <p>{ sprintf ('%02u:%02u', minutes, seconds) }</p>
  : <p>{ sprintf ('%02u:%02u:%02u', hours, minutes, seconds) }</p>
    }
}
