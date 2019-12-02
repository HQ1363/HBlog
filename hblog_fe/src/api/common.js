import Vue from 'vue'
import { dataResolver, errorHandler, urlPrefix } from '@/plugins/axios'

const commonAPI = {}

commonAPI.base = (method, uri, responseType = 'json', params = {}, body = {}) => {
  return Vue.axios({
    method: method,
    baseURL: urlPrefix,
    url: uri,
    params: params,
    data: body,
    // `transformRequest` 允许在向服务器发送前，修改请求数据
    // 只能用在 'PUT', 'POST' 和 'PATCH' 这几个请求方法
    // 后面数组中的函数必须返回一个字符串，或 ArrayBuffer，或 Stream
    transformRequest: [function (data) {
      // 对 request data 进行任意转换处理
      return data
    }],
    // `transformResponse` 在传递给 then/catch 前，允许修改响应数据
    transformResponse: [function (data) {
      // 对 response data 进行任意转换处理
      return data
    }],
    // 3s超时
    timeout: 3000,
    responseType: responseType,
    withCredentials: true
  }).then(dataResolver)
    .catch(errorHandler)
}

export default commonAPI
