<template>

    <metainfo>
      <template v-slot:title="{ content }">{{ content }}</template>
    </metainfo>

    <div v-if="fullScreenLoading" class="fullscreen-loading">Loading&#8230;</div>

    <div class="Login">
        <div class="container">

            <div class="row shadow-lg my-2">

                <div class="col-md-6 d-flex align-items-center gradient-custom-2">
                    <div class="text-white px-3 py-4 p-md-5 mx-md-4">
                        <h4 class="mb-4">کتاب خوار با افتخار تقدیم میکند.</h4>
                        <p class="small mb-0">هدف از راه اندازی کتاب خوار ترغیب ایرانیان به کتاب و کتاب خوانی است. با پیوستن به کتاب خوار خود را غرق در دنیای کتاب کنید.</p>
                    </div>
                </div>

                <div class="col-md-6 p-5">
                    
                    <div class="text-center">
                        <h1><span class="badge bg-warning">کتاب خوار</span></h1>
                        <p>برای ثبت نام لطفا اطلاعات خود را وارد کنید.</p>
                    </div>


                    <!-- register form -->
                    <form @submit.prevent="doRegister()">
                        <label class="form-label" for="floatingUsername">نام کاربری</label>
                        <div class="form-floating mb-3" dir="ltr" lang="en">
                            <input 
                                v-model="username"
                                type="text" 
                                class="form-control" 
                                id="floatingUsername" 
                                placeholder="نام کاربری"
                                :class="{'is-invalid':usernameE===true, 'is-valid':usernameE===false}">


                            <label for="floatingUsername">Username</label>

                            <div class="invalid-feedback">
                                {{ usernameEM }}
                            </div>
                        </div>

                        <label class="form-label" for="floatingEmail">ایمیل</label>
                        <div class="form-floating mb-3" dir="ltr" lang="en">
                            <input 
                                v-model="email"
                                type="text" 
                                class="form-control" 
                                id="floatingEmail" 
                                placeholder="ایمیل"
                                :class="{'is-invalid':emailE===true, 'is-valid':emailE===false}"
                            >


                            <label for="floatingEmail">Email</label>

                            <div class="invalid-feedback">
                                {{ emailEM }}
                            </div>
                        </div>

                        <label class="form-label" for="floatingPassword1">رمز عبور</label>
                        <div class="form-floating mb-3" dir="ltr" lang="en">
                            <input 
                                v-model="password"
                                type="password" 
                                class="form-control" 
                                id="floatingPassword1" 
                                placeholder="رمز عبور"
                                :class="{'is-invalid':passwordE===true, 'is-valid':passwordE===false}"
                            >

                            <button type="button" @click="showPassword('floatingPassword1')" class="btn"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-eye-fill" viewBox="0 0 16 16"><path d="M10.5 8a2.5 2.5 0 1 1-5 0 2.5 2.5 0 0 1 5 0z"/><path d="M0 8s3-5.5 8-5.5S16 8 16 8s-3 5.5-8 5.5S0 8 0 8zm8 3.5a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7z"/></svg></button>

                            <label for="floatingPassword1">password</label>

                            <div class="invalid-feedback">
                                {{ passwordEM }}
                            </div>
                        </div>

                        <label class="form-label" for="floatingpasswordConfirm">تایید رمز عبور</label>
                        <div class="form-floating" dir="ltr" lang="en">
                            <input 
                                v-model="passwordConfirm"
                                type="password" 
                                class="form-control" 
                                id="floatingpasswordConfirm" 
                                placeholder="تایید رمز عبور"
                                :class="{'is-invalid':passwordConfirmE===true, 'is-valid':passwordConfirmE===false}"
                            >

                            <button type="button" @click="showPassword('floatingpasswordConfirm')" class="btn"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-eye-fill" viewBox="0 0 16 16"><path d="M10.5 8a2.5 2.5 0 1 1-5 0 2.5 2.5 0 0 1 5 0z"/><path d="M0 8s3-5.5 8-5.5S16 8 16 8s-3 5.5-8 5.5S0 8 0 8zm8 3.5a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7z"/></svg></button>

                            <label for="floatingpasswordConfirm">Confirm password</label>

                            <div class="invalid-feedback">
                                {{ passwordConfirmEM }}
                            </div>
                        </div>

                        <div class="d-flex justify-content-between">
                            <button type="submit" class="btn btn-outline-success my-3">ثبت نام</button>
                            <router-link to="/login" class="btn btn-outline-primary text-decoration-none my-3">حساب کاربری دارم!</router-link>
                        </div>

                    </form>
                    <!-- end of register form -->
                    

                    <div class="text-center mb-3">
                        <p>ثبت نام با استفاده از:</p>
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
            </div>

        </div>
    </div>
</template>


<script>
import { ref } from "vue";
import axios from 'axios';
import { useMeta } from 'vue-meta'

export default {
    setup() {
        useMeta({
            title: "ثبت نام در کتاب خوار",
            description: "شما عزیزان با ورود به کتاب خوار میتوانید از خدماتی از قبیل رای به کتاب ها, کامنت, و منتشر کردن رای های خود برای دیگران بهرمند شوید.",
            robots: "index, follow",
            keywords: "کتاب خوار, کتاب, نویسنده, نقد کتاب, کتابخانه, دسته بندی های کتاب, برترین کتاب ها",
            googlebot: "index, follow",
            author: "امین مهری",
            owner: "امین مهری",
            canonical: "https://bookeater.ir/register",
            'og:type': "register-bookeater",
            'og:title': "bookeater",
            'og:description': "شما عزیزان با ورود به کتاب خوار میتوانید از خدماتی از قبیل رای به کتاب ها, کامنت, و منتشر کردن رای های خود برای دیگران بهرمند شوید.",
            'og:site_name': "ثبت نام در کتاب خوار",
            'og:url': "https://bookeater.ir/register",
            'og:image': "https://bookeater.ir/media/image.jpg",
            'twitter:title': "ثبت نام در کتاب خوار",
            'twitter:description': "شما عزیزان با ورود به کتاب خوار میتوانید از خدماتی از قبیل رای به کتاب ها, کامنت, و منتشر کردن رای های خود برای دیگران بهرمند شوید.",
            'twitter:site': "https://twitter.com/aminem_mehri",
            'twitter:card': "Summary Card",
            'twitter:image': "https://bookeater.ir/media/image.jpg",
        });

        let username = ref('')
        let password = ref('')
        let passwordConfirm = ref('')
        let email = ref('')

        let usernameE = ref()
        let usernameEM = ref('')
        let passwordE = ref()
        let passwordEM = ref('')
        let passwordConfirmE = ref()
        let passwordConfirmEM = ref('')
        let emailE = ref()
        let emailEM = ref('')

        let fullScreenLoading = ref(false)


        function doRegister() {
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

            
            if(email.value.indexOf('@') == -1 || email.value.indexOf('.') == -1){
                emailE.value = true
                access = false
                if(email.value.length == 0){
                    emailEM.value = 'ایمیل اجباری است'
                } else{
                    emailEM.value = 'لطفا ایمیل خود را به صورت صحیح وارد کنید'
                }
            } else if(email.value.length < 6){
                emailE.value = true
                access = false
                emailEM.value = 'لطفا ایمیل خود را به صورت صحیح وارد کنید'
            } else {
                emailE.value = false
                emailEM.value = ''
            }


            if(password.value.length < 8){
                passwordE.value = true
                access = false
                if(password.value.length == 0){
                    passwordEM.value = 'رمزعبور اجباری است'
                } else {
                    passwordEM.value = 'رمزعبور باید بیشتر از ۷ کاراکتر باشد'
                }
            } else {
                passwordE.value = false
                passwordEM.value = ''
            }


            if(passwordConfirm.value.length < 8){
                passwordConfirmE.value = true
                access = false
                if(passwordConfirm.value.length == 0){
                    passwordConfirmEM.value = 'تکرار رمزعبور اجباری است'
                } else {
                    passwordConfirmEM.value = 'تکراررمزعبور باید بیشتر از ۷ کاراکتر باشد'
                }
            } else {
                passwordConfirmE.value = false
                passwordConfirmEM.value = ''
            }


            if(password.value != passwordConfirm.value){
                access = false
                passwordE.value = true
                passwordConfirmE.value = true
                passwordEM.value = 'رمزعبور و تکرار آن با هم مطابقت ندارد'
            } else {
                if(!passwordE.value && passwordConfirmE.value) {
                    access = true
                }
            }

            if(access){
                fullScreenLoading.value = true
                axios
                    .post('dj-rest-auth/registration/', {
                        username: username.value,
                        password1: password.value,
                        password2: passwordConfirm.value,
                        email: email.value,
                    })
                    .then(response => {
                        // store.commit('login', response.data.access_token)
                        fullScreenLoading.value = false
                        axios
                        .post('SendEmail/', {
                            username: username.value,
                            email: email.value
                        })
                        .then(response => {
                            Swal.fire({
                                icon: 'success',
                                title: 'ایمیل تایید برای شما فرستاده شد.',
                                text: '',
                                backdrop: false,
                                timer: 2000,
                                showConfirmButton: false,
                            })
                        })
                        .catch(error => {
                            console.log(error.response);
                        })

                    })
                    .catch(error => {
                        console.log(error.response);
                        fullScreenLoading.value = false
                        
                        if(error.response){
                            if(error.response.status == 400){
                            
                                if(error.response.data['username']){
                                    if(error.response.data['username'][0] == "A user with that username already exists."){
                                        usernameE.value = true
                                        usernameEM.value = "کاربر با نام کاربری شما موجود است"

                                    }
                                } else if(error.response.data['email']){
                                    if(error.response.data['email'][0] == 'A user is already registered with this e-mail address.'){
                                        emailE.value = true
                                        emailEM.value = "کاربری با ایمیل شما موجود است."
                                    }
                                } else if(error.response.data['password1']){
                                   
                                    if(error.response.data['password1'][0] == 'This password is too common.'){
                                        passwordE.value = true
                                        passwordConfirmE.value = true
                                        passwordEM.value = "این رمزعبور بسیار رایج است لطفا تغییرش دهید."
                                    } else if(error.response.data['password1'][0] == 'This password is entirely numeric.'){
                                        console.log("kif2");
                                        passwordE.value = true
                                        passwordConfirmE.value = true
                                        passwordEM.value = "این رمزعبور همش عدده. لامصب عوضش کن."
                                    }
                                    
                                }
                                
                                
                            } else{
                                usernameE.value = true
                                usernameEM.value = "یه مشکلی پیش اومده. لطفا صبر کن."
                            }
                        }
                    })

            }
            
        } 

        function showPassword(input) {
            let x = document.getElementById(input)
            if (x.type === "password") {
                x.type = "text";
            } else {
                x.type = "password";
            }
        }


        return{
            doRegister,
            showPassword,
            username,
            password,
            passwordConfirm,
            email,
            usernameE,
            usernameEM,
            passwordE,
            passwordEM,
            passwordConfirmE,
            passwordConfirmEM,
            emailE,
            emailEM,
            fullScreenLoading,
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