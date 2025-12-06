import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { createPinia } from 'pinia'
import '@/assets/style.css'
import 'element-plus/theme-chalk/el-message.css'   // 仅消息样式
import { ElMessage } from 'element-plus'

const app = createApp(App)
app.use(createPinia()).use(router)
app.config.globalProperties.$message = ElMessage   // 全局挂载
app.mount('#app')
createApp(App).use(router).use(createPinia()).mount('#app')