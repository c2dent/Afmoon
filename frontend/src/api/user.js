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
		return HTTP.post('/phone_login/login/', { 'phone_number': String(user.phone_number), 'password': String(user.password1) }).
		then(response => {
			console.log(response)
			return response
		})
	},
	create_user (user_data) {
		return HTTP.post('/phone_login/generate/', {'nickname': String(user_data.nickname),
		 'phone_number': String(user_data.phone_number), 'password': String(user_data.password)
	}).
		then(response => {
			console.log(response)
			return response
		})
	},
	validate_user (user_valid) {
		return HTTP.post('/phone_login/registration/', {'phone_number': String(user_valid.phone_number), 'otp': String(user_valid.otp) }).
		then((response) => {
			console.log(response)
			return response
		})
	}
}