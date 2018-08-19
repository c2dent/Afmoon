// eslint-disable-next-line
/* eslint-disable */
import { HTTP } from './common'

export const Ad = {
  create (config) {
    return HTTP.post('/ad/', config).then(response => {
      return response.data
    })
  },
  delete (ad) {
    return HTTP.delete(`/ad/${ad.id}/`)
  },
  list (region, category, id) {
    if ( category == undefined  &&  id == undefined) {
      return HTTP.get(`/${region}/`).then(response => {
        return response.data
      })
    } else if (id == undefined) {
      return HTTP.get(`/${region}/${category}/`).then(response => {
        return response.data
    })
    } else {
      return HTTP.get(`/${region}/${category}/${id}/`).then(response => {
        return response.data
    })
    }
  }
}