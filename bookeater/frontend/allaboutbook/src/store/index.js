import { createStore } from 'vuex'
import axios from 'axios'

export default createStore({
  state: {
    isAuthenticated: true,
    token: ''
  },
  mutations: {
    login(state, token) {
      state.isAuthenticated = true
      state.token = token
      localStorage.setItem("access", token)
      axios.defaults.headers.common['Authorization'] = "Bearer " + token
    },
    logout(state) {
      state.isAuthenticated = false
      state.token = ''
      axios.defaults.headers.common['Authorization'] = ""
      localStorage.removeItem("access")
    },
  },
  actions: {
    onStart (context) {
      let token = localStorage.getItem("access")
      if (token) {
        axios.defaults.headers.common['Authorization'] = "Bearer " + token
        axios
          .get('ShowProfile/')
          .then(response => {
            context.commit('login', token)
          })
          .catch(error => {
            context.commit('logout')
          })
      } else {
        context.commit('logout')
      }
    }
  },
  modules: {
  }
})
