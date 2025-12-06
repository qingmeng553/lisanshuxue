import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { resolve } from 'path'

export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': resolve(__dirname, 'src'),   // ← 关键
    },
  },
  server: {
    proxy: {
      '/api': 'http://127.0.0.1:8000',   // 后端地址
    },
  },
})