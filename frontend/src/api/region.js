// eslint-disable-next-line
/* eslint-disable */

import { HTTP } from './common'
export const Regions = {
  list () {
    return HTTP.get('/ads/1/region/').then(response => {
      return response.data
    })
  }
}