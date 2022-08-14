import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import 'bootstrap/dist/css/bootstrap.min.css';
import 'jquery/src/jquery.js';
import 'popper.js/dist/popper.min.js';
import 'bootstrap/dist/js/bootstrap.bundle';
import VueSweetalert2 from 'vue-sweetalert2';


axios.defaults.baseURL = 'http://127.0.0.1:8000';

createApp(App).use(store).use(router).use(VueSweetalert2).mount('#app')
