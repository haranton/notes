import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  server: {
    proxy: {
      '/api': {  // Перенаправлять /api запросы на FastAPI
        target: 'http://localhost:8000',
        changeOrigin: true
      }
    }
  }
})