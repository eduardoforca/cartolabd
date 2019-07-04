import axios from 'axios'

export default async ({ Vue }) => {
  Vue.prototype.$axios = axios
  Vue.prototype.$api = axios.create({
    baseURL: 'http://157.230.153.79/v1/'
  })
}
