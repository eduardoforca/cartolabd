import store from '../store/index'
const routes = [
  {
    path: '/',
    component: () => import('layouts/default.vue'),
    redirect: '/home',
    beforeEnter: (to, from, next) => {
      store.dispatch('user/fetchUser')
      if (store.state.user.user === null) {
        next('/login')
      } else {
        next()
      }
    },
    children: [
      { path: 'home', component: () => import('pages/Index.vue'), name: 'Home' },
      { path: 'myteam',
        component: () => import('pages/Team.vue'),
        name: 'Equipe',
        redirect: '/myteam/manage',
        beforeEnter: (to, from, next) => {
          if (store.state.user.team === null && to.path !== '/myteam/new') {
            next('/myteam/new')
          } else {
            next()
          }
        },
        children: [
          { path: 'new', component: () => import('components/team/TeamBuilder.vue'), name: 'Novo Time' },
          { path: 'manage', component: () => import('components/team/TeamManager.vue'), name: 'Gerenciar Time' }
        ]
      },
      { path: 'leagues',
        component: () => import('pages/Leagues.vue'),
        name: 'Ligas',
        children: [
          { path: '', component: () => import('components/league/LeaguesHome.vue'), name: 'Minhas Ligas' },
          { path: 'new', component: () => import('components/league/LeagueBuilder.vue'), name: 'Nova Liga' },
          { path: 'manage/:league_id', component: () => import('components/league/LeagueManager.vue'), name: 'Gerenciar Liga' }
        ]
      },
      { path: 'matches', component: () => import('pages/Matches.vue'), name: 'Partidas' },
      { path: 'profile', component: () => import('pages/Profile.vue'), name: 'Perfil' }
    ]
  },
  {
    path: '/login',
    component: () => import('layouts/Login.vue'),
    beforeEnter: (to, from, next) => {
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
