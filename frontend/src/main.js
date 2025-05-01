import { createApp } from 'vue'  // Импорт функции создания приложения
import App from './App.vue'     // Импорт корневого компонента

// Создание и монтирование приложения
const app = createApp(App)

// Опционально: подключение плагинов, глобальных компонентов и т.д.
// app.use(router)      // Пример: Vue Router
// app.use(pinia)       // Пример: Pinia (стейт-менеджер)

// Монтирование в DOM-элемент с id="app" (в public/index.html)
app.mount('#app')