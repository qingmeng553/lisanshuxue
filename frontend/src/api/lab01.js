import axios from 'axios'

export function getTruthTable(data) {
  return axios({
    method: 'post',
    url: '/api/lab01/truth_table/',
    headers: {
      'Content-Type': 'application/json',
      Authorization: 'Bearer ' + localStorage.getItem('token')   // ← 钉死
    },
    data
  })
}