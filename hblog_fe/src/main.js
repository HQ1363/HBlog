import Vue from 'vue'
import './plugins/axios'
import App from './App.vue'
import router from './router'
import store from './store'
import './plugins/element.js'
// 过滤器
import filters from '@/utils/filters'
// 引入全局css
import '@assets/iconfont/iconfont'
import './global.less'
// 引入markdown编辑器
import mavonEditor from 'mavon-editor'
import 'mavon-editor/dist/css/index.css'
// 引入vue-ls组件
import VueStorage from 'vue-ls'

const options = {
  namespace: 'hblog__', // key prefix
  name: 'ls', // name variable Vue.[ls] or this.[$ls],
  storage: 'local' // storage name session, local, memory
}
Vue.use(VueStorage, options)

Vue.use(mavonEditor)

/* eslint-disable */
Vue.config.productionTip = false
filters(Vue)

// 必须单独打印env才可以看到值，否则还看不到值
console.log('process env: ', process.env)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
