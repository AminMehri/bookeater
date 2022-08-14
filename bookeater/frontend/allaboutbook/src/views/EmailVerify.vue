<template>
    <!-- <p class="alert alert-danger">ایمیل شما تایید شد</p> -->
</template>


<script>
import { ref, onMounted } from 'vue'
import { useStore } from 'vuex'
import { useRoute, useRouter } from 'vue-router';
import axios from 'axios'
import Swal from 'sweetalert2'


export default {
	setup() {
        const store = useStore()
        const route = useRoute();
        const router = useRouter();
        
        function getData(){
            axios
            .post('VerifyEmail/', {
                slug: route.params.token
            })
            .then(response => {
                Swal.fire({
                    icon: 'success',
                    title: 'ایمیل شما با موفقیت تایید شد.',
                    text: '',
                    backdrop: false,
                    timer: 2000,
                    showConfirmButton: false,
                })
                router.push('/login')
            })
            .catch(error => {
                console.log(error.response)
                if (error.response.status == 'token is not exist or expired'){
                    Swal.fire({
                        icon: 'danger',
                        title: 'توکن شما اشتباه یا باطل شده است',
                        text: '',
                        backdrop: false,
                        timer: 2000,
                        showConfirmButton: false,
                    })
                }
                store.commit('logout')
                router.push('/register')
            })
        }
        getData()


		return {
            getData

		}
    
	},

}

</script>