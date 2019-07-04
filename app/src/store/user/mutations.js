export function setUser (state, { user, keep = false }) {
  if (keep) {
    window.localStorage.setItem('user', JSON.stringify(user))
  } else {
    window.sessionStorage.setItem('user', JSON.stringify(user))
  }
  state.user = user
}

export function setTeam (state, { team }) {
  state.team = team
}

export function setToken (state, { token, keep = false }) {
  if (keep) {
    window.localStorage.setItem('token', token)
  } else {
    window.sessionStorage.setItem('token', token)
  }
  state.token = token
}

export function unsetToken (state) {
  window.localStorage.removeItem('token')
  window.sessionStorage.removeItem('token')
  state.token = null
}

export function unsetUser (state) {
  window.localStorage.removeItem('user')
  window.sessionStorage.removeItem('user')
  state.user = null
}

export function unsetTeam (state) {
  state.team = null
}
