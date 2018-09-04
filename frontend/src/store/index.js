// frontend/src/store/index.js
import Vue from 'vue'
import Vuex from 'vuex'
import { Ad } from '../api/ads'
import { User } from '../api/user'
import axios from 'axios'
import {
  ADD_AD,
  REMOVE_AD,
  SET_ADS,
  AUTH_REQUEST,
  AUTH_SUCCESS,
  AUTH_ERROR,
  SET_OWNER,
  AUTH_LOGOUT,
  REGIS_USER
} from './mutation-types.js'

// eslint-disable-next-line
/* eslint-disable */

Vue.use(Vuex)

// Состояние
const state = {
  ads: [] , // список заметок
  token: localStorage.getItem('user-token') || '',
  status: '',
  profile : {},
  phone_number : ''
}

// Геттеры
const getters = {
  ads: state => state.ads  ,// получаем список заметок из состояния
  isAuthenticated: state => !!state.token,
  authStatus: state => state.status,
  profile : state => state.profile,
  phone_number : state => state.phone_number
}

// Мутации
const mutations = {
  // Добавляем заметку в список
  [ADD_AD] (state, ad) {
    state.ads = [ad, ...state.ads]
  },
  // Убираем заметку из списка
  [REMOVE_AD] (state, { id }) {
    state.ads = state.ads.filter(ad => {
      return ad.id !== id
    })
  },
  // Задаем список заметок
  [SET_ADS] (state, { ads }) {
    state.ads = ads
  },
  [SET_OWNER] (state , { profile }) {
    state.profile = profile
  },
  [AUTH_REQUEST] (state) {
    state.status = 'loading,'
  },
  [AUTH_SUCCESS] (state, {token}) {
    state.status = 'success',
    state.token = token
  },
  [AUTH_ERROR] (state) {
    state.status = 'error'
  },
  [AUTH_LOGOUT] (state) {
    state.status = undefined
  },
  [REGIS_USER] (state, {phone_number}) {
    state.phone_number = phone_number
  }
}

// Действия
const actions = {

  createAds ({ commit }, adData) {
    Ad.create(adData).then(ad => {
      commit(ADD_AD, ad)
    })
  },
  deleteAd ({ commit }, ad) {
    Ad.delete(ad).then(response => {
      commit(REMOVE_AD, ad)
    })
  },
  getAds ({ commit }, param) {
    Ad.list(param[0],param[1],param[2]).then(ads => {
      commit(SET_ADS, { ads })
    })
  },
  getOwner ({ commit }) {
    User.owner().then(profile => {
      commit(SET_OWNER, { profile })
      console.log(response)
    })
  },
  loginUser ({commit}, user) {
    User.login(user).then(resp => {
      const token = resp.data.token
      commit(AUTH_REQUEST)
      console.log(resp)
      localStorage.setItem('user-token', resp.data.token)
      axios.defaults.headers.common['Authorization'] = 'Bearer ' +  token
      commit(AUTH_SUCCESS, {token})
      return resp
    } ).catch(err => {
      commit (AUTH_ERROR)
      localStorage.removeItem('user-token')
      return err
    })
  },
  logout ({commit}) {
    return new Promise ((resolve, reject) => {
      commit(AUTH_LOGOUT)
      localStorage.removeItem('user-token') // clear your user's token from localstorage
      resolve()
    })
  },
  create_user ({commit}, user_data) {
    User.create_user(user_data).then(response => {
      const phone_number = response.data
      localStorage.setItem('phone_number', phone_number)
      console.log(response)
      commit(REGIS_USER, {phone_number})
      return response
    }).catch(err => {
      console.log(err)
      return err
    })
  },
  validate_user (state, user_valid) {
    User.validate_user ({'phone_number': localStorage.getItem('phone_number'), 'otp': user_valid.otp}).then(response => {
      console.log(response)
      return response
    }).catch (error => {
      console.log(error)
      return error
    }) 
  },
  loginer ({commit}) {
    commit(AUTH_REQUEST)
    localStorage.setItem('blala ', 'bloagfd')
  }
}

export default new Vuex.Store({
  state,
  getters,
  actions,
  mutations,
})
