import { createRouter, createWebHistory } from 'vue-router'
import Login from './views/Login.vue'
import SelectLab from './views/SelectLab.vue'
import Lab01 from './views/Lab01.vue'
import Lab02 from './views/Lab02.vue'
const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', redirect: '/login' },
    { path: '/login', component: Login },
    { path: '/select', component: SelectLab, meta: { needAuth: true } },
    { path: '/lab01', component: Lab01, meta: { needAuth: true } },
    { path: '/lab02', component: Lab02, meta: { needAuth: true } },
  ]
})

router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('token')
  if (to.meta.needAuth && !token) return next('/login')
  next()
})

export default router