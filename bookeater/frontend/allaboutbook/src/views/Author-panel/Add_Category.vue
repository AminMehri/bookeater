<template>

    <div v-if="loading" class="fullscreen-loading">Loading&#8230;</div>

    <div class="row g-0">

        <Sidebar />

        <div class="col-sm-8 col-md-9 col-lg-10 p-3 mt-3">
            <h3 class="text-center">اضافه کردن دسته بندی</h3>
            <div class="row g-3 border p-4">

                <div class="col-md-6">
                    <label for="inputCategory" class="form-label">نام دسته بندی</label>
                    <input v-model="title" type="text" class="form-control" id="inputCategory">
                </div>

                <div class="col-md-6">
                    <label for="inputSlug" class="form-label">اسلاگ</label>
                    <input v-model="slug" type="text" class="form-control" id="inputSlug">
                </div>

                <div class="col-md-6">
                    <label for="id_author" class="form-label ms-3">نویسنده های مرتبط:</label>
                    <select v-model="author" name="author" required="" id="id_author" multiple="">

                        <option v-for="author in authors" :value="`${author.id}`">{{author.full_name}}</option>

                    </select>
                </div>

                <div class="col-md-6"></div>

                <div class="col-12">
                    <label for="inputDescription" class="form-label">توضیحات</label>
                    <!-- <textarea v-model="description" class="form-control" id="inputDescription" rows="6"></textarea> -->
                    <ckeditor v-model="description" class="form-control" id="inputDescription" :editor="editor"></ckeditor>
                </div>
                
                <div class="col-12">
                    <label for="inputContent" class="form-label">محتوا</label>
                    <!-- <textarea v-model="content" class="form-control" id="inputContent" rows="10"></textarea> -->
                    <ckeditor v-model="content" class="form-control" id="inputContent" :editor="editor"></ckeditor>
                </div>

                <div class="col-md-6">
                    <div class="input-group mb-3 align-items-center">
                        <label for="inputThumbnail" class="form-label ms-3">عکس بند انگشتی:</label>
                        <input type="file" class="form-control" id="inputThumbnail">
                    </div>
                </div>

                <div class="col-md-6">
                    <div class="input-group mb-3 align-items-center">
                        <label for="inputImage" class="form-label ms-3">عکس اصلی: </label>
                        <input type="file" class="form-control" id="inputImage">
                    </div>
                </div>

                <div class="col-md-6">
                    <div class="input-group mb-3 align-items-center">
                        <label for="id_status" class="form-label ms-3">وضعیت: </label>
                        <select v-model="status" class="form-select" id="id_status">
                            <option value="d">پیش نویس</option>
                            <option value="s">ارسال به ادمین</option>
                        </select>
                    </div>
                </div>

                <div class="col-12">
                    <button @click="sendData()" class="btn btn-primary">تایید</button>
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
import ClassicEditor from '@ckeditor/ckeditor5-build-classic';
import Sidebar from '@/components/Sidebar.vue'

export default{
    components: {
        Sidebar
    },
    setup() {
        const store = useStore()
        const route = useRoute()
        const router = useRouter()

        let authors = ref('')

        let title = ref('')
        let slug = ref('')
        let author = ref('')
        let description = ref('')
        let content = ref('')
        let status = ref()

        let editor = ClassicEditor

        let slugForEdit = ref(route.params.slug) 

        let loading = ref(false)

        if(slugForEdit.value == 'new-category'){
            
        }else {
            loading.value = true
            axios
            .post('ShowSingleCategoryEditPanel/', {
                slug: slugForEdit.value
            })
            .then(response => {
                title.value = response.data.data[0].title
                slug.value = response.data.data[0].slug
                description.value = response.data.data[0].description
                content.value = response.data.data[0].content
                loading.value = false
            })
            .catch(error => {
                if(error.response.status == 400 || error.response.status == 404){
                    Swal.fire({
                        icon: 'warning',
                        title: 'دسته بندی با این اسلاگ وجود ندارد',
                        backdrop: false,
                        timer: 2500,
                        showConfirmButton: false,
                    })
                    router.push('/author-panel')
                }
                if(error.response.status == 406){
                    Swal.fire({
                        icon: 'warning',
                        title: 'شما قادر به ادیت این دسته بندی نیستید',
                        backdrop: false,
                        timer: 2500,
                        showConfirmButton: false,
                    })
                    router.push('/author-panel')
                }
                loading.value = false
            })
        }

        function getData(){
            axios
            .get('ShowAllAuthors/')
            .then(response => {
                authors.value = response.data.data
            })
            .catch(error => {
                console.log(error.response);
            })
        }
        getData()


        function sendData(){
            loading.value = true

            let formData = new FormData()
            let thumbnailPic = document.getElementById('inputThumbnail')
            let imagePic = document.getElementById('inputImage')

            formData.append('title', title.value)
            formData.append('slug', slug.value)
            formData.append('author', author.value)
            formData.append('description', description.value)
            formData.append('content', content.value)
            formData.append('status', status.value)
            formData.append('thumbnail', thumbnailPic.files[0])
            formData.append('image', imagePic.files[0])

            axios
            .post('AddCategoryPanel/', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            })
            .then(response => {
                title.value = ''
                slug.value = ''
                description.value = ''
                content.value = ''
                loading.value = false

                Swal.fire({
                    icon: 'success',
                    title: 'ثبت دسته بندی موفقیت انجام شد.',
                    backdrop: false,
                    timer: 1500,
                    showConfirmButton: false,
                    position: 'top',
                })

                router.push('/author-panel/categories')
            })
            .catch(error => {
                if(error.response.status == 406){
                    Swal.fire({
                    icon: 'warning',
                    title: 'دسته بندی با این اسلاگ موجود است',
                    backdrop: false,
                    timer: 2500,
                    showConfirmButton: false,
                    })
                }

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
            authors,
            title,
            slug,
            author,
            description,
            content,
            status,
            editor,
            loading,
            getData,
            sendData,
        }
    }
}
</script>