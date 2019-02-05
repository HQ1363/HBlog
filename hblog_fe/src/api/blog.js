import Vue from 'vue'

import { dataResolver, errorHandler } from '@/plugins/axios'

const blogApi = {}

blogApi.getBlogList = () => {
  return Vue.axios.get('/server/api/blog/article', {
    withCredentials: true
  }).then(dataResolver).catch(errorHandler)
}

blogApi.getBlogDetail = id => {
  return Vue.axios.get(`/server/api/blog/article/${id}`, {
    withCredentials: true
  }).then(dataResolver).catch(errorHandler)
}

export default blogApi
