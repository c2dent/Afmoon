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
  AUTH_LOGOUT
} from './mutation-types.js'

// eslint-disable-next-line
/* eslint-disable */

Vue.use(Vuex)

// Состояние
const state = {
  ads: [] , // список заметок
  token: localStorage.getItem('user-token') || '',
  status: '',
  profile : {}
}

// Геттеры
const getters = {
  ads: state => state.ads  ,// получаем список заметок из состояния
  isAuthenticated: state => !!state.token,
  authStatus: state => state.status,
  profile : state => state.profile
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
