import store from '../store/index'
const routes = [
  {
    path: '/',
    component: () => import('layouts/default.vue'),
    redirect: '/home',
    beforeEnter: async (to, from, next) => {
      store.dispatch('user/fetchUser')
      if (store.state.user.user === null) {
        next('/login')
      } else {
        next()
      }
    },
    children: [
      { path: 'home', component: () => import('pages/Index.vue'), name: 'Home' }
    ]
  },
  {
    path: '/login',
    component: () => import('layouts/Login.vue'),
    beforeEnter: async (to, from, next) => {
      store.dispatch('user/fetchUser')
      if (store.state.user.user !== null) {
        next('/')
      } else {
        next()
      }
    },
    children: [
      { path: '/login', component: () => import('pages/Signin.vue') },
      { path: '/sign', component: () => import('pages/Signup.vue') }
    ]
  }
]

// Always leave this as last one
if (process.env.MODE !== 'ssr') {
  routes.push({
    path: '*',
    component: () => import('pages/Error404.vue')
  })
}

export default routes
