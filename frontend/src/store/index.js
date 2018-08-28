// frontend/src/store/index.js
import Vue from 'vue'
import Vuex from 'vuex'
import { Ad } from '../api/ads'
import { User } from '../api/user'
import {
  ADD_AD,
  REMOVE_AD,
  SET_ADS,
  AUTH_REQUEST,
  AUTH_SUCCESS,
  AUTH_ERROR
} from './mutation-types.js'

// eslint-disable-next-line
/* eslint-disable */

Vue.use(Vuex)

// Состояние
const state = {
  ads: [] , // список заметок
  token: localStorage.getItem('csrftoken') || '',
  status: '',
}

// Геттеры
const getters = {
  ads: state => state.ads  ,// получаем список заметок из состояния
  isAuthenticated: state => !!state.token,
  authStatus: state => state.status
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
  [AUTH_REQUEST] (state) {
    state.status = 'loading,'
  },
  [AUTH_SUCCESS] (state, {token}) {
    state.status = 'success',
    state.token = token
  },
  [AUTH_ERROR] (state) {
    state.status = 'error'
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
    console.log('men seni soyyan')
    Ad.list(param[0],param[1],param[2]).then(ads => {
      commit(SET_ADS, { ads })
    })
  },
  loginUser ({commit}, user) {
    commit(AUTH_REQUEST)
    User.login(user).then(resp => {
      const token = resp.data.token
      localStorage.setItem('user-token', token)
      console.log(resp)
      axios.defaults.headers.common['Authorization'] = token
      commit(AUTH_SUCCESS, {token})
      return resp
    } ).catch(err => {
      commit (AUTH_ERROR)
      localStorage.removeItem('user-token')
      return err
    })
  },
}

export default new Vuex.Store({
  state,
  getters,
  actions,
  mutations,
})
