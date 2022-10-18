<template>
    <Navbar />
    <router-view/>
	<Footer />
</template>


<script>
import { useStore } from 'vuex'
import { useRoute, useRouter } from 'vue-router'
import { ref, onMounted } from "vue";
import Navbar from './components/Navbar.vue'
import Footer from './components/Footer.vue'
import axios from 'axios'



export default {
	components: {
		Navbar,
		Footer,
    },
	setup() {
		const store = useStore()
    	const route = useRoute()
		const router = useRouter()

		onMounted(() => {
			store.dispatch('onStart')
        })

    
		return {
			
		}

    },
	watch: {
		$route() {
			this.$store.dispatch('onStart')
		},

	},

}

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
}

a{
    text-decoration: none !important;
}
</style>
