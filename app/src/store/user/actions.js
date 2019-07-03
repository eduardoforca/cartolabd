export function fetchUser ({ commit, dispatch, state, getters }) {
  let user = JSON.parse(window.localStorage.getItem('user'))
  if (user) {
    commit('setUser', user)
  }
}

export function loginUser ({ commit, dispatch, state, getters }, { user }) {
  commit('setUser', user)
}

export function setUser ({ commit, dispatch, state, getters }, { user }) {
  commit('setUser', user)
}

export function logoutUser ({ commit }) {
  commit('unsetUser')
}
