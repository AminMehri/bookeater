<template>

    <div v-if="loading" class="fullscreen-loading">Loading&#8230;</div>

    <div class="row g-0">

        <Sidebar />


        <div class="col-sm-8 col-md-9 col-lg-10 p-3 mt-3">
            <h3 class="text-center">اضافه کردن نقل قول</h3>
            <div class="row g-3 border p-4">

                <div class="col-md-6">
                    <label for="inputAuthor" class="form-label">نویسنده</label>
                    <input v-model="fullName" type="text" class="form-control" id="inputAuthor">
                </div>

                <div class="col-12">
                    <label for="inputDescription" class="form-label">توضیحات</label>
                    <!-- <textarea v-model="description" class="form-control" id="inputDescription" rows="6"></textarea> -->
                    <ckeditor v-model="description" class="form-control" id="inputDescription" :editor="editor"></ckeditor>
                </div>

                <div class="col-md-6">
                    <div class="input-group mb-3 align-items-center">
                        <label for="inputThumbnail" class="form-label ms-3">عکس بند انگشتی نویسنده:</label>
                        <input type="file" class="form-control" id="inputThumbnail">
                    </div>
                </div>

                <div class="col-12">
                    <button @click="sendData()" class="btn btn-primary">ارسال به ادمین</button>
                </div>
            </div>
        </div>
        
    </div>
</template>


<script>
import { ref } from "vue";
import { useRouter } from 'vue-router'
import axios from 'axios'
import Swal from 'sweetalert2'
import ClassicEditor from '@ckeditor/ckeditor5-build-classic';
import Sidebar from '@/components/Sidebar.vue'

export default{
    components: {
        Sidebar
    },
    setup() {
        const router = useRouter()

        let fullName = ref('')
        let description = ref('')

        let editor = ClassicEditor

        let loading = ref(false)

        function sendData(){
            loading.value = true

            let formData = new FormData()
            let thumbnailPic = document.getElementById('inputThumbnail')

            formData.append('fullName', fullName.value)
            formData.append('description', description.value)
            formData.append('thumbnail', thumbnailPic.files[0])

            axios
            .post('AddQuotePanel/', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            })
            .then(response => {
                fullName.value = ''
                description.value = ''
                loading.value = false
                
                Swal.fire({
                    icon: 'success',
                    title: 'ثبت نقل قول موفقیت انجام شد.',
                    backdrop: false,
                    timer: 1500,
                    showConfirmButton: false,
                    position: 'top',
                })

                router.push('/author-panel/quotes')
            })
            .catch(error => {
                if(error.response.status == 400){
                    Swal.fire({
                    icon: 'warning',
                    title: 'همشو پر کن دیوص کونی',
                    backdrop: false,
                    timer: 2500,
                    showConfirmButton: false,
                    })
                }
                loading.value = false
            })
        } 
        
        return{
            fullName,
            description,
            editor,
            loading,
            sendData,
        }
    }
}
</script>