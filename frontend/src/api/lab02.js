import axios from 'axios'

const api = axios.create({ baseURL: '/api' })

// 请求拦截：带 JWT
api.interceptors.request.use(config => {
  const token = localStorage.getItem('token')
  if (token) config.headers.Authorization = `Bearer ${token}`
  return config
})

export default {
  calculate(matrix) {
    return api.post('/lab02/calculate/', { matrix })
  }
}