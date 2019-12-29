'use strict'

import Vue from 'vue'
import axios from 'axios'
import { Message, Loading } from 'element-ui'

// export const urlPrefix = 'http://www.hblog.com:8000/api'
export const urlPrefix = process.env.baseURL || process.env.apiUrl || ''

let loading
function startLoading () {
  // console.log('开始请求')
  loading = Loading.service({
    lock: true,
    text: '拼命加载中...',
    background: 'rgba(0,0,0,0.7)'
  })
}

function endLoading () {
  // console.log('结束请求')
  loading.close()
}

export function dataResolver (res) {
  return res.data
}

export function errorHandler (error) {
  if (error.response) {
    // 请求已发出，但服务器响应的状态码不在 2xx 范围内
    // console.log(error.response.data)
    let errorCode = error.response.status
    switch (errorCode) {
      case 403:
        console.log('没有权限访问')
        break
      case 401:
        console.log('认证未通过，请先登录')
        break
      case 400:
        console.log('请求错误：', error.response.data.message)
        break
      case 500:
        console.log('服务器错误，请联系管理员')
        break
      default:
        console.log('未知错误')
    }
    // console.log(error.response.headers)
    Message.error(error.response.data.message || '请求失败')
  } else {
    // Something happened in setting up the request that triggered an Error
    Message.error('请求失败')
  }
  // console.log(error.config)
}

let config = {
  baseURL: urlPrefix,
  timeout: 60 * 1000, // Timeout
  withCredentials: true // Check cross-site Access-Control
}

const _axios = axios.create(config)

_axios.interceptors.request.use(
  function (config) {
    startLoading()
    // Do something before request is sent
    return config
  },
  function (error) {
    // Do something with request error
    endLoading()
    return Promise.reject(error)
  }
)

// Add a response interceptor
_axios.interceptors.response.use(
  function (response) {
    // Do something with response data
    endLoading()
    return response
  },
  function (error) {
    // Do something with response error
    endLoading()
    return Promise.reject(error)
  }
)

function get (url, params = {}) {
  return new Promise((resolve, reject) => {
    axios.get(url, {
      params: params
    })
      .then(response => {
        resolve(response.data)
      })
      .catch(err => {
        reject(err)
      })
  })
}

/**
 * 封装post请求
 * @param url
 * @param data
 * @returns {Promise}
 */
function post (url, data = {}) {
  return new Promise((resolve, reject) => {
    axios.post(url, data)
      .then(response => {
        resolve(response.data)
      }, err => {
        reject(err)
      })
  })
}

Plugin.install = function (Vue, options) {
  Vue.axios = _axios
  window.axios = _axios
  Object.defineProperties(Vue.prototype, {
    axios: {
      get: () => {
        return _axios
      }
    },
    $axios: {
      get: () => {
        return _axios
      }
    },
    $get: get,
    $post: post
  })
}

Vue.use(Plugin)

export default Plugin
