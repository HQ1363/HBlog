import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/visitor',
    name: 'visitor',
    component: () => import(/* webpackChunkName: "about" */ '../views/visitor/Index.vue')
  },
  {
    path: '/admin',
    name: 'admin',
    component: () => import(/* webpackChunkName: "about" */ '@views/admin/Index.vue'),
    children: [
      {
        path: 'statistic',
        name: 'statistic',
        component: () => import('@views/admin/statistic/Index.vue')
      },
      {
        path: 'document',
        name: 'document',
        component: () => import('@views/admin/document/Index.vue')
      },
      {
        path: 'user',
        name: 'user',
        component: () => import('@views/admin/user/Index.vue')
      },
      {
        path: 'system',
        name: 'system',
        component: () => import('@views/admin/system/Index.vue')
      }
    ]
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
