<template>
    <div class="Password-reset-confirm">
        <div class="container">
            <div class="row">
                <div class="col-md-8 mx-auto border-start border-end p-5 my-4 shadow-lg" style="text-align: justify;">

                    <div class="row border p-2">

                        <div class="col-md-12">
                            <label for="inputResetPassword1" class="form-label">رمزعبور جدید</label>
                            <input v-model="resetPassword1" type="text" class="form-control" id="inputResetPassword1" >
                        </div>

                        <div class="col-md-12">
                            <label for="inputResetPassword2" class="form-label my-2">تایید رمزعبور</label>
                            <input v-model="resetPassword2" type="text" class="form-control" id="inputResetPassword2" >
                        </div>
                        
                    </div>
                    <button @click="resetPasswordConfirm()" class="btn btn-outline-success fw-bold mt-3 w-25">Submit</button>

                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { useRoute, useRouter } from 'vue-router'
import { ref } from "vue";
import axios from 'axios'
import Swal from 'sweetalert2'


export default {
	setup() {
        const route = useRoute()
        const router = useRouter()

        let resetPassword1 = ref()
        let resetPassword2 = ref()

        let uid = ref(route.params.uid)
        let token = ref(route.params.token)


        function resetPasswordConfirm(){
            axios
                .post(`dj-rest-auth/password/reset/confirm/`, {
                    new_password1: resetPassword1.value,
                    new_password2: resetPassword2.value,
                    uid: uid.value,
                    token: token.value
                })
                .then(response => {
                    Swal.fire({
                        title: 'YEEY',
                        text:   "رمزعبور شما با موفقیت تغییر یافت.",
                        icon: 'success',
                    });
                    router.push('/login')
                })
                .catch(error => {
                    Swal.fire({
                        title: 'OPPS',
                        text:   "لطفا اطلاعات خود را به درستی وارد کنید. همچنین ممکن است توکن شما منقضی شده باشد.",
                        icon: 'warning',
                    });
                })
        }


        return {
            resetPasswordConfirm,
            resetPassword1,
            resetPassword2,
        }
	},
}

</script>

<style scoped>
.Password-reset-confirm{
    background-color: rgb(142, 210, 255);
}

.border-start{
    background-color: rgb(172, 222, 255);
}
</style>