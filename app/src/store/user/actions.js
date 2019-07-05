import axios from 'axios'
export async function fetchUser ({ commit, dispatch, state, getters }) {
  let token = window.localStorage.getItem('token')
  if (token) {
    await dispatch('loginUser', { token: token, keep: true })
  } else {
    token = window.sessionStorage.getItem('token')
    if (token) {
      await dispatch('loginUser', { token: token })
    }
  }
}

export async function loginUser ({ commit, dispatch, state, getters }, { token, keep = false }) {
  commit('setToken', { token: token, keep: keep })
  axios.defaults.headers.common['Authorization'] = 'Token ' + token
  let response = await axios.get('api/usuarios/me')
  if (response.status === 200) {
    commit('setUser', { user: response.data })
  } else {
    throw response.statusText
  }
}

export function setUser ({ commit, dispatch, state, getters }, { user }) {
  commit('setUser', { user: user })
}

export function setTeam ({ commit, dispatch, state, getters }, { team }) {
  commit('setTeam', { team: team })
}

export function logoutUser ({ commit }) {
  commit('unsetUser')
  commit('unsetToken')
}
