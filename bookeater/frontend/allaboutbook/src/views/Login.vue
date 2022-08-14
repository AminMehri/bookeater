<template>
    <div class="Login">
        <div class="container">

            <div class="row shadow-lg my-2">
                <div class="col-md-6 p-5">
                    
                    <div class="text-center">
                        <h1><span class="badge bg-warning">همه چیز درباره کتاب</span></h1>
                        <p>لطفا اطلاعات خود را وارد کنید.</p>
                    </div>


                    <!-- login form -->
                    <form @submit.prevent="doLogin()">
                        <label class="form-label" for="floatingUsername">نام کاربری</label>
                        <div class="form-floating mb-3" dir="ltr" lang="en">
                            <input 
                                v-model="username" 
                                type="text" 
                                class="form-control" 
                                id="floatingUsername" 
                                placeholder="نام کاربری"
                                :class="{'is-invalid':usernameE===true, 'is-valid':usernameE===false}"
                            >

                            <label for="floatingUsername">Username</label>
                            <div class="invalid-feedback">
                                {{ usernameEM }}
                            </div>
                        </div>

                        <label class="form-label" for="floatingPassword">رمز عبور</label>
                        <div class="form-floating" dir="ltr" lang="en">
                            <input 
                                v-model="password" 
                                type="password" 
                                class="form-control" 
                                id="floatingPassword" 
                                placeholder="رمز عبور"
                                :class="{'is-invalid':passwordE===true, 'is-valid':passwordE===false}"
                            >

                            <label for="floatingPassword">password</label>
                            <div class="invalid-feedback">
                                {{ passwordEM }}
                            </div>
                        </div>


                        <div class="d-flex justify-content-between">
                            <button type="submit" class="btn btn-outline-success my-3">ورود به حساب کاربری</button>
                            <router-link to="/register" class="btn btn-outline-primary text-decoration-none my-3">عضو سایت نیستم!</router-link>
                        </div>

                    </form>
                    <!-- end login form -->

                    <!-- Button trigger modal -->
                    <button type="button" class="btn btn-outline-warning" data-bs-toggle="modal" data-bs-target="#exampleModal">
                        رمزعبورمو فراموش کردم!
                    </button>

                    <!-- Modal -->
                    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                        <div class="modal-dialog">
                            <div class="modal-content">
                                <div class="modal-header">
                                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                </div>
                                <div class="modal-body">
                                    <input v-model="email" class="w-100 form-control" type="text" placeholder="لطفا ایمیل خود را وارد کنید">
                                </div>
                                <div class="modal-footer">
                                    <button @click="doForgetPassword()" type="button" class="btn btn-outline-primary">تایید ایمیل</button>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="text-center mb-3">
                        <p>ورود با استفاده از:</p>
                        <button type="button" class="btn btn-link btn-floating mx-1">
                            <i class="fab fa-facebook-f"></i>
                        </button>

                        <button type="button" class="btn btn-link btn-floating mx-1">
                            <i class="fab fa-google"></i>
                        </button>

                        <button type="button" class="btn btn-link btn-floating mx-1">
                            <i class="fab fa-twitter"></i>
                        </button>

                        <button type="button" class="btn btn-link btn-floating mx-1">
                            <i class="fab fa-github"></i>
                        </button>
                    </div>

                </div>

                <div class="col-md-6 d-flex align-items-center gradient-custom-2">
                    <div class="text-white px-3 py-4 p-md-5 mx-md-4">
                        <h4 class="mb-4">همه چیز درباره کتاب با افتخار تقدیم میکند.</h4>
                        <p class="small mb-0">هدف از راه اندازی همه چیز درباره کتاب ترغیب ایرانیان به کتاب و کتاب خوانی است. با پیوستن به همه چیز درباره کتاب از دنیای کتاب نهایت استفاده را ببرید</p>
                    </div>
                </div>
            </div>

        </div>
    </div>
</template>


<script>
import { onMounted, ref } from "vue";
import { useStore } from 'vuex'
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'
import Swal from 'sweetalert2'

export default{
    setup() {
        const store = useStore()
        const route = useRoute()
        const router = useRouter()


        let username = ref('')
        let password = ref('')
        let usernameE = ref()
        let passwordE = ref()
        let usernameEM = ref('')
        let passwordEM = ref('')

        let email = ref('')
        let resetPasswordEM = ref('')


        function isAuthenticated(){
            if(store.state.isAuthenticated){
                router.push('/profile')
            }
        }
        isAuthenticated()


        function doLogin() {
            let access = true
            if(username.value.length < 5){
                usernameE.value = true
                access = false
                if(username.value.length == 0){
                    usernameEM.value = 'نام کاربری اجباری است'
                } else {
                    usernameEM.value = 'نام کاربری باید بالای ۴ کاراکتر باشد'
                }
            } else {
                usernameE.value = false
                usernameEM.value = ''
            }

            if(password.value.length < 8){
                passwordE.value = true
                access = false
                if(password.value.length == 0){
                    passwordEM.value = 'رمز اجباری است'
                } else {
                    passwordEM.value = 'رمز باید بالای ۷ کاراکتر باشد'
                }
            } else {
                passwordE.value = false
                passwordEM.value = ''
            }

            if(access){

                axios
                    .post('dj-rest-auth/login/', {
                        username: username.value,
                        password: password.value
                    })
                    .then(response => {
                        store.commit('login', response.data.access_token)
                        router.push('/profile')
                    })
                    .catch(error => {
                        if (error.response.data.non_field_errors.join(" ") == "Unable to log in with provided credentials."){
                            usernameEM.value = "!نام کاربری یا رمزعبورتو اشتباه زدی. دقت کن"
                        }

                        usernameE.value = true
                        passwordE.value = true
                    })

            }
        }   

        function doForgetPassword(){
            axios
                .post('dj-rest-auth/password/reset/', {
                    email: email.value,
                })
                .then(response => {
                    Swal.fire({
                        icon: 'success',
                        title: 'هورا!!!',
                        text: 'ایمیل برای شما ارسال شد.',
                    })

                    location.reload()
                })
                .catch(error => {
                    if(error.response.statusText == 'Bad Request'){
                        resetPasswordEM.value = 'ایمیلی که وارد کردی اشتباهه. تصحیحش کن.'
                    } else{
                        resetPasswordEM.value = 'یه جای کار میلنگه'
                    }
                    Swal.fire({
                        icon: 'error',
                        title: 'وای!!!',
                        text: resetPasswordEM.value,
                    })

                    console.log(error.response.statusText)
                })
        }
        
        return{
            username,
            password,
            usernameE,
            passwordE,
            usernameEM,
            passwordEM,
            email,
            doLogin,
            doForgetPassword,
            isAuthenticated,
        }
    }
}
</script>



<style scoped>
.gradient-custom-2 {
background: #fccb90;

/* Chrome 10-25, Safari 5.1-6 */
background: -webkit-linear-gradient(to right, #ee7724, #d8363a, #dd3675, #b44593);

/* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
background: linear-gradient(to right, #ee7724, #d8363a, #dd3675, #b44593);
}
</style>