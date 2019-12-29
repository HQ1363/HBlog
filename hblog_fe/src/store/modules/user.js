import Vue from 'vue'
import {
  ACCESS_TOKEN,
  USER
} from '@/store/mutations'
import userApi from '@/api/user'

const user = {
  state: {
    token: null,
    user: {
      name: 'HQ'
    }
  },
  getters: {
    username (state, getters, rootState, rootGetters) {
      return state.user.name
    }
  },
  mutations: {
    SET_TOKEN: (state, token) => {
      Vue.ls.set(ACCESS_TOKEN, token)
      state.token = token
    },
    CLEAR_TOKEN: state => {
      Vue.ls.remove(ACCESS_TOKEN)
      state.token = null
    },
    SET_USER: (state, user) => {
      Vue.ls.set(USER, user)
      state.user = user
    }
  },
  actions: {
    loadUser ({ commit, dispatch }) {
      return new Promise((resolve, reject) => {
        userApi
          .getProfile()
          .then(response => {
            commit('SET_USER', response.data.data)
            resolve(response)
          })
          .catch(error => {
            reject(error)
          })
      })
    },
    login ({ commit, dispatch }, { username, password }) {
      return new Promise((resolve, reject) => {
        userApi
          .login(username, password)
          .then(response => {
            const token = response.data.data
            Vue.$log.debug('Got token', token)
            commit('SET_TOKEN', token)

            resolve(response)
          })
          .catch(error => {
            reject(error)
          })
      })
    },
    logout ({ commit, dispatch }) {
      return new Promise(resolve => {
        commit('CLEAR_TOKEN')
        userApi
          .logout()
          .then(response => {
            resolve()
          })
          .catch(() => {
            resolve()
          })
      })
    }
  }
}

export default user
