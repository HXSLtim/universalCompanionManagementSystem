import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { createRouter, createWebHistory } from 'vue-router'
import ArcoVue from '@arco-design/web-vue'
import '@arco-design/web-vue/dist/arco.css'
import './style.css'
import App from './App.vue'

// Create pinia instance
const pinia = createPinia()

// Create router instance
const router = createRouter({
  history: createWebHistory(),
  routes: [
    // Define your routes here
    // Example:
    // { path: '/', component: () => import('./views/Home.vue') }
  ]
})

const app = createApp(App)

app.use(pinia)
app.use(router)
app.use(ArcoVue)

app.mount('#app')