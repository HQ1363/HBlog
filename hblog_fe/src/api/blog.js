import Vue from 'vue'

import { dataResolver, errorHandler } from '@/plugins/axios'

const blogApi = {}

blogApi.getBlogs = () => {
  Vue.axios.get('/server/api/blog/article', {
    withCredentials: true
  }).then(dataResolver).catch(errorHandler)
}

export default blogApi
