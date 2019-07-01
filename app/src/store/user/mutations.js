export function setUser (state, user) {
  window.localStorage.setItem('user', JSON.stringify(user))
  state.user = user
}

export function unsetUser (state) {
  window.localStorage.removeItem('user')
  state.user = null
}
