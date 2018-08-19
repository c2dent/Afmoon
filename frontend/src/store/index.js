// frontend/src/store/index.js
import Vue from 'vue'
import Vuex from 'vuex'
import { Ad } from '../api/ads'
import {
  ADD_AD,
  REMOVE_AD,
  SET_ADS
} from './mutation-types.js'

// eslint-disable-next-line
/* eslint-disable */

Vue.use(Vuex)

// Состояние
const state = {
  ads: [] , // список заметок
}

// Геттеры
const getters = {
  ads: state => state.ads  ,// получаем список заметок из состояния
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
  }
}

export default new Vuex.Store({
  state,
  getters,
  actions,
  mutations,
})
