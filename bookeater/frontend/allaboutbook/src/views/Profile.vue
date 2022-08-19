<template>
    <div class="container Profile">
        <div class="row g-3">

            <div class="col-md-6 border p-4 mt-4 shadow">

                <label for="inputUserName" class="form-label">نام کاربری</label>
                <input type="text" class="form-control" id="inputUserName" disabled :value="`${username}`">

                <label for="inputEmail" class="form-label">ایمیل</label>
                <input type="text" class="form-control" disabled :value="`${email}`" id="inputEmail" >

                <label for="inputFullName" class="form-label">نام و نام خانوادگی</label>
                <input type="text" class="form-control" disabled :value="`${fullName}`" id="inputFullName" >

                <label for="inputage" class="form-label">سن</label>
                <input type="text" class="form-control" disabled :value="`${age}`" id="inputage" >

                <label for="inputsex" class="form-label">جنسیت</label>
                <input type="text" class="form-control" disabled :value="`${sex}`" id="inputsex" >

                <label for="inputpublicScore" class="form-label">نشان دادن نمره های شما به دیگران</label>
                <input type="text" class="form-control" disabled :value="`${publicScore}`" id="inputpublicScore" >

                <button class="btn fw-bold btn-outline-danger my-2 w-100" @click="doLogout">خروج از سایت</button>
                <button class="btn fw-bold btn-outline-warning my-2 w-100" data-bs-toggle="modal" data-bs-target="#staticBackdrop">ویرایش اطلاعات</button>
                <router-link v-if="isAuthor" to="/author-panel" class="btn btn-outline-info fw-bold w-100 my-2">رفتن به پنل نویسنده ها</router-link>

            </div>

            <div class="col-md-6">
                <div class="card">
                    
                </div>
            </div>
    
        </div>

        <div class="modal fade" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="staticBackdropLabel">ویرایش اطلاعات</h5>
                    </div>
                    <div class="modal-body">


                        <div class="row g-3">
                            <div class="col-md-6">
                                <label for="inputUserName" class="form-label">نام کاربری</label>
                                <input type="text" class="form-control" id="inputUserName" disabled :value="`${username}`">
                            </div>

                            <div class="col-md-6">
                                <label for="inputFirstName" class="form-label">نام</label>
                                <input v-model="updateFirstName" type="text" class="form-control" id="inputFirstName" >
                            </div>

                            <div class="col-md-6">
                                <label for="inputLastName" class="form-label">نام خانوادگی</label>
                                <input v-model="updateLastName" type="text" class="form-control" id="inputLastName" >
                            </div>

                            <div class="col-md-6">
                                <label for="inputSex" class="form-label">جنسیت</label>
                                <select v-model="updateSex" class="form-select" aria-label="Default select example">
                                    <option value="f">زن</option>
                                    <option value="m">مرد</option>
                                </select>
                            </div>

                            <div class="col-md-6">
                                <label for="inputAge" class="form-label">سن</label>
                                <input v-model="updateAge" type="text" class="form-control" id="inputAge">
                            </div>

                            <div class="col-md-6">
                                <label for="inputPublicScore" class="form-label">قابل رویت بودن نمره های شما برای دیگران</label>
                                <select v-model="updatePublicScore" class="form-select" aria-label="Default select example">
                                    <option value="true">بله</option>
                                    <option value="false">خیر</option>
                                </select>
                            </div>

                            <div class="">
                                <div class="input-group mb-3 align-items-center">
                                    <label for="inputThumbnail" class="form-label ms-3">عکس آواتار:</label>
                                    <input type="file" class="form-control" id="inputThumbnail">
                                </div>
                            </div>

                            <div class="">
                                <div class="input-group mb-3 align-items-center">
                                    <label for="inputImage" class="form-label ms-3">عکس خطی: </label>
                                    <input type="file" class="form-control" id="inputImage">
                                </div>
                            </div>
                            
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button id="closeButton" type="button" class="btn btn-secondary" data-bs-dismiss="modal">بستن</button>
                        <button @click="updateInfo()" class="btn fw-bold bg-success">ویرایش</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
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

        let username = ref('')
        let email = ref('')
        let fullName = ref('')
        let sex = ref('')
        let age = ref('')
        let publicScore = ref('')
        let isAuthor = ref()

        let updateFirstName = ref('')
        let updateLastName = ref('')
        let updateSex = ref('')
        let updateAge = ref('')
        let updatePublicScore = ref('')
        
        function getData(){
            axios
            .get('ShowProfile/')
            .then(response => {
                username.value = response.data.data[0].username
                email.value = response.data.data[0].email
                fullName.value = response.data.data[0].full_name
                sex.value = response.data.data[0].sex
                age.value = response.data.data[0].age
                publicScore.value = response.data.data[0].public_score
                isAuthor.value = response.data.data[0].is_author

                if(sex.value == 'm'){
                    sex.value = 'مرد'
                } else if(sex.value == 'f'){
                    sex.value = 'زن'
                }

                if(age.value == 0){
                    age.value = ''
                }

                if(publicScore.value == false){
                    publicScore.value = 'خیر'
                } else{
                    publicScore.value = 'بله'
                }
            })
            .catch(error => {
                console.log(error.response)
                store.commit('logout')
                router.push('/login')
            })
        }
        getData()

        function doLogout() {
            axios
            .post('dj-rest-auth/logout/')
            .then(response => {
                store.commit('logout')
                router.push('/login')
            })
            .catch(error => {
                console.log(error.response)
            })
        }



        function updateInfo(){
            let formData = new FormData()
            let thumbnailPic = document.getElementById('inputThumbnail')
            let imagePic = document.getElementById('inputImage')

            formData.append('first_name', updateFirstName.value)
            formData.append('last_name', updateLastName.value)
            formData.append('age', updateAge.value)
            formData.append('sex', updateSex.value)
            formData.append('public_score', updatePublicScore.value)
            formData.append('thumbnail', thumbnailPic.files[0])
            formData.append('image', imagePic.files[0])

            axios
            .put('UpdateProfileInformation/', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            })
            .then(response => {
                Swal.fire({
                    icon: 'success',
                    title: 'اطلاعات شما با موفقیت تغییر یافت.',
                    showConfirmButton: false,
                    backdrop: false,
                    timer: 1500,
                });
                document.getElementById('closeButton').click()
                getData()
            })
            .catch(error => {
                console.log(updatePublicScore.value)

                console.log(error.response)
                Swal.fire({
                    icon: 'warning',
                    title: 'لطفا اطلاعات خود به صورت درست وارد نمایید.',
                    backdrop: false,
                    timer: 1500,
                    showConfirmButton: false,
                });
            })

        }

		return {
            username,
            email,
            fullName,
            sex,
            age,
            publicScore,
            isAuthor,

            updateFirstName,
            updateLastName,
            updateSex,
            updateAge,
            updatePublicScore,

			doLogout,
            getData,
            updateInfo,

		}
    
	},

}

</script>
