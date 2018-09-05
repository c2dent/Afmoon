// eslint-disable-next-line
/* eslint-disable */

import { HTTP } from './common'
export const Navigations = {
  list_region () {
    return HTTP.get('/region/').then(response => {
      return response.data
    })
  },
  list_category () {
    return HTTP.get('/category/').then(response => {
      return response.data
    })
  }
}