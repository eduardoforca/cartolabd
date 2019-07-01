export async function fetchUser ({ commit, dispatch, state, getters }) {
  let user = JSON.parse(window.localStorage.getItem('user'))
  if (user) {
    commit('setUser', user)
  }
}
export async function loginUser ({ commit, dispatch, state, getters }, { user }) {
  commit('setUser', user)
}
export async function logoutUser ({ commit }) {
  commit('unsetUser')
}
