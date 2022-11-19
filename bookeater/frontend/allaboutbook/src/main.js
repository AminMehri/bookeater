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
import CKEditor from '@ckeditor/ckeditor5-vue';
import { createMetaManager } from 'vue-meta'


axios.defaults.baseURL = 'https://api.bookeater.ir';
// axios.defaults.baseURL = 'http://127.0.0.1:8000';

createApp(App).use(store).use(router).use(VueSweetalert2).use(CKEditor).use(
    createMetaManager(false, {
    body: {
        tag: "script",
        to: "body",
    },
    base: {
        valueAttribute: "href",
    },
    charset: {
        tag: "meta",
        nameless: true,
        valueAttribute: "charset",
    },
    description: {
        tag: "meta",
    },
    keywords: {
        tag: "meta",
    },
    robots: {
        tag: "meta",
    },
    googlebot: {
        tag: "meta",
    },
    'og:type': {
        tag: "meta",
        keyAttribute: "property",
    },
    'og:title': {
        tag: "meta",
        keyAttribute: "property",
    },
    'og:description': {
        tag: "meta",
        keyAttribute: "property",
    },
    'og:url': {
        tag: "meta",
        keyAttribute: "property",
    },
    'og:site_name': {
        tag: "meta",
        keyAttribute: "property",
    },
    'og:image': {
        tag: "meta",
        keyAttribute: "property",
    },
    'twitter:title': {
        tag: "meta",
    },
    'twitter:description': {
        tag: "meta",
    },
    'twitter:card': {
        tag: "meta",
    },
    'twitter:site': {
        tag: "meta",
    },
    'twitter:image': {
        tag: "meta",
    },
    author: {
        tag: "meta"
    },
    owner: {
        tag: "meta"
    },
    canonical: {
        keyAttribute: "rel",
        tag: "link"
    },
    htmlAttrs: {
        attributesFor: "html",
    },
    headAttrs: {
        attributesFor: "head",
    },
    bodyAttrs: {
        attributesFor: "body",
    },
    })
).mount('#app')

