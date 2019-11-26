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
    component: () => import(/* webpackChunkName: "about" */ '../views/admin/Index.vue'),
    children: [
      {
        path: 'tag',
        name: 'tag',
        component: () => import('../views/admin/Tag.vue')
      },
      {
        path: 'blog',
        name: 'blog',
        component: () => import('../views/admin/Blog.vue')
      },
      {
        path: 'comment',
        name: 'comment',
        component: () => import('../views/admin/Comment.vue')
      },
      {
        path: 'category',
        name: 'category',
        component: () => import('../views/admin/Category.vue')
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
