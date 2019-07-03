import axios from 'axios'
export function fetchUser ({ commit, dispatch, state, getters }) {
  let user = JSON.parse(window.localStorage.getItem('user'))
  if (user) {
    commit('setUser', { user: user, keep: true })
  } else {
    user = JSON.parse(window.sessionStorage.getItem('user'))
    if (user) {
      commit('setUser', { user: user })
    }
  }
}

export async function loginUser ({ commit, dispatch, state, getters }, { token, keep }) {
  commit('setToken', { token: token, keep: keep })
  let response = await axios.post('http://157.230.153.79/v1/me/',
    {
      token: token
    })
  if (response.status === 200) {
    commit('setUser', { user: response.data, keep: keep })
  } else {
    throw response.statusText
  }
}

export function setUser ({ commit, dispatch, state, getters }, { user }) {
  commit('setUser', { user: user })
}

export function logoutUser ({ commit }) {
  commit('unsetUser')
  commit('unsetToken')
}
