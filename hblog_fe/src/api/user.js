import Vue from 'vue'

import { dataResolver, errorHandler } from '@/plugins/axios'

const userApi = {}

userApi.getProfile = () => {
  return Vue.axios.get('/server/api/user', {
    withCredentials: true
  }).then(dataResolver).catch(errorHandler)
}

userApi.login = () => {
  return Vue.axios.post('/server/api/login', {}, {
    withCredentials: true
  }).then(dataResolver).catch(errorHandler)
}

userApi.logout = () => {
  return Vue.axios.post('/server/api/logout', {}, {
    withCredentials: true
  }).then(dataResolver).catch(errorHandler)
}

export default userApi
