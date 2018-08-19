// eslint-disable-next-line
/* eslint-disable */

import { HTTP } from './common'
export const Catigories = {
  list () {
    return HTTP.get('/category/').then(response => {
      return response.data
    })
  }
}