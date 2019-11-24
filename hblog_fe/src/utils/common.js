export default window.dialog = {
  alert: function (content) {
    window.alert(content)
  },
  confirm: function (content) {
    return window.confirm(content)
  },
  prompt: function (content, auto = 'null') {
    return window.prompt(content, auto)
  }
}

export function checkType (object) {
  const usuallyType = [Number, String, Boolean, Function]
  let currentType = typeof object
  if (usuallyType.indexOf(currentType) !== -1) {
    return currentType
  }
  if (object !== null && object !== undefined) {
    return object.constructor
  }
  return Object.prototype.toString.call(object)
}

export function getCurrentDatetime () {
  let now = new Date()
  let year = now.getFullYear()
  let month = now.getMonth() + 1
  let day = now.getDate()
  let hh = now.getHours() // 时
  let mm = now.getMinutes() // 分
  let ss = now.getSeconds() // 秒
  let clock = year + '-'

  if (month < 10) {
    clock += '0'
  }
  clock += month + '-'

  if (day < 10) {
    clock += '0'
  }

  clock += day + ' '

  if (hh < 10) {
    clock += '0'
  }
  clock += hh + ':'

  if (mm < 10) {
    clock += '0'
  }
  clock += mm

  if (ss < 10) {
    clock += '0'
  }
  clock += ss
  return clock
}

export function setCookie (cname, cvalue, exdays) {
  let d = new Date()
  d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000))
  let expires = 'expires=' + d.toGMTString()
  document.cookie = cname + '=' + cvalue + '; ' + expires
}

export function getCookie (cname) {
  let name = cname + '='
  let ca = document.cookie.split(';')
  for (let i = 0; i < ca.length; i++) {
    let c = ca[i].trim()
    if (c.indexOf(name) === 0) return c.substring(name.length, c.length)
  }
  return ''
}

export function delCookie (name, options) {
  options = options || {}
  options['expires'] = new Date(0)
  return this.set(name, '', options)
}

export function saveLocalStorage (key, value) {
  if (value instanceof String || typeof value === 'string') {
    window.localStorage.setItem(key, value)
  } else {
    const tmpValue = JSON.stringify(value)
    window.localStorage.setItem(key, tmpValue)
  }
}

export function getLocalStorage (key) {
  const infoStr = localStorage.getItem(key)
  return JSON.parse(infoStr)
}

export function delLocalStorage (key) {
  window.localStorage.removeItem(key)
  // window.localStorage.clear()
}
