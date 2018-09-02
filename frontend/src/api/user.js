// eslint-disable-next-line
/* eslint-disable */
import { HTTP } from './common'

export const User = {
	owner () {
		return HTTP.get('/profile/').then(response => {
			return response.data
		})
	},
	login (user) {
		return HTTP.post('/phone_login/login/', { 'phone_number': String(user.phone_number), 'password': String(user.password) }).
		then(response => {
			return response
		})
	}
}