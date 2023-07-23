import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './index.css'

createApp(App).use(router).mount('#app')

document.documentElement.classList.add('dark') // force dark mode
