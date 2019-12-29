import Vue from 'vue'
import Vuex from 'vuex'

import user from './modules/user'

import getters from './getters'

Vue.use(Vuex)

export default new Vuex.Store({
  // 开启严格模式
  strict: true,
  state: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    user
  },
  getters
})
