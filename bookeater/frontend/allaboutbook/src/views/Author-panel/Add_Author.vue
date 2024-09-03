<template>

    <div v-if="loading" class="fullscreen-loading">Loading&#8230;</div>

    <div class="row g-0">

        <Sidebar />

        <div class="col-sm-8 col-md-9 col-lg-10 p-3 mt-3">
            <h3 class="text-center">اضافه کردن نویسنده</h3>
            <div class="row g-3 border p-4">

                <div class="col-md-6">
                    <label for="inputAuthor" class="form-label">نام نویسنده</label>
                    <input v-model="fullName" type="text" class="form-control" id="inputAuthor">
                </div>

                <div class="col-md-6">
                    <label for="inputSlug" class="form-label">اسلاگ</label>
                    <input v-model="slug" type="text" class="form-control" id="inputSlug">
                </div>

                <div class="col-md-6">
                    <label for="id_category" class="form-label ms-3">دسته بندی های مرتبط:</label>
                    <select v-model="category" name="category" required="" id="id_category" multiple="">

                        <option v-for="category in categories" :value="`${category.id}`">{{category.title}}</option>

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
import { ref } from "vue";
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
        const route = useRoute()
        const router = useRouter()

        let categories = ref('')

        let fullName = ref('')
        let slug = ref('')
        let category = ref('')
        let description = ref('')
        let content = ref('')
        let status = ref()

        let editor = ClassicEditor

        let slugForEdit = ref(route.params.slug) 

        let loading = ref(false)

        if(slugForEdit.value == 'new-author'){
            
        }else {
            loading.value = true
            axios
            .post('ShowSingleAuthorEditPanel/', {
                slug: slugForEdit.value
            })
            .then(response => {
                fullName.value = response.data.data[0].full_name
                slug.value = response.data.data[0].slug
                description.value = response.data.data[0].description
                content.value = response.data.data[0].content
                loading.value = false
            })
            .catch(error => {
                if(error.response.status == 400 || error.response.status == 404){
                    Swal.fire({
                        icon: 'warning',
                        title: 'نویسنده ای با این اسلاگ وجود ندارد',
                        backdrop: false,
                        timer: 2500,
                        showConfirmButton: false,
                    })
                    router.push('/author-panel')
                }
                if(error.response.status == 406){
                    Swal.fire({
                        icon: 'warning',
                        title: 'شما قادر به ادیت این نویسنده نیستید',
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
            .get('ShowAllCategories/')
            .then(response => {
                categories.value = response.data.data
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

            formData.append('fullName', fullName.value)
            formData.append('slug', slug.value)
            formData.append('category', category.value)
            formData.append('description', description.value)
            formData.append('content', content.value)
            formData.append('status', status.value)
            formData.append('thumbnail', thumbnailPic.files[0])
            formData.append('image', imagePic.files[0])

            axios
            .post('AddAuthorPanel/', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            })
            .then(response => {
                fullName.value = ''
                slug.value = ''
                description.value = ''
                content.value = ''
                loading.value = false


                Swal.fire({
                    icon: 'success',
                    title: 'ثبت نویسنده موفقیت انجام شد.',
                    backdrop: false,
                    timer: 1500,
                    showConfirmButton: false,
                    position: 'top',
                })

                router.push('/author-panel/authors')
            })
            .catch(error => {
                if(error.response.status == 406){
                    Swal.fire({
                    icon: 'warning',
                    title: 'نویسنده با این اسلاگ موجود است',
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
            categories,
            fullName,
            slug,
            category,
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


<style>
/* Absolute Center Spinner */
.fullscreen-loading {
  position: fixed;
  z-index: 999;
  height: 2em;
  width: 2em;
  overflow: show;
  margin: auto;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
}

/* Transparent Overlay */
.fullscreen-loading:before {
  content: '';
  display: block;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
    background: radial-gradient(rgba(20, 20, 20,.8), rgba(0, 0, 0, .8));

  background: -webkit-radial-gradient(rgba(20, 20, 20,.8), rgba(0, 0, 0,.8));
}

/* :not(:required) hides these rules from IE9 and below */
.fullscreen-loading:not(:required) {
  /* hide "loading..." text */
  font: 0/0 a;
  color: transparent;
  text-shadow: none;
  background-color: transparent;
  border: 0;
}

.fullscreen-loading:not(:required):after {
  content: '';
  display: block;
  font-size: 10px;
  width: 1em;
  height: 1em;
  margin-top: -0.5em;
  -webkit-animation: spinner 150ms infinite linear;
  -moz-animation: spinner 150ms infinite linear;
  -ms-animation: spinner 150ms infinite linear;
  -o-animation: spinner 150ms infinite linear;
  animation: spinner 150ms infinite linear;
  border-radius: 0.5em;
  -webkit-box-shadow: rgba(255,255,255, 0.75) 1.5em 0 0 0, rgba(255,255,255, 0.75) 1.1em 1.1em 0 0, rgba(255,255,255, 0.75) 0 1.5em 0 0, rgba(255,255,255, 0.75) -1.1em 1.1em 0 0, rgba(255,255,255, 0.75) -1.5em 0 0 0, rgba(255,255,255, 0.75) -1.1em -1.1em 0 0, rgba(255,255,255, 0.75) 0 -1.5em 0 0, rgba(255,255,255, 0.75) 1.1em -1.1em 0 0;
box-shadow: rgba(255,255,255, 0.75) 1.5em 0 0 0, rgba(255,255,255, 0.75) 1.1em 1.1em 0 0, rgba(255,255,255, 0.75) 0 1.5em 0 0, rgba(255,255,255, 0.75) -1.1em 1.1em 0 0, rgba(255,255,255, 0.75) -1.5em 0 0 0, rgba(255,255,255, 0.75) -1.1em -1.1em 0 0, rgba(255,255,255, 0.75) 0 -1.5em 0 0, rgba(255,255,255, 0.75) 1.1em -1.1em 0 0;
}

/* Animation */

@-webkit-keyframes spinner {
  0% {
    -webkit-transform: rotate(0deg);
    -moz-transform: rotate(0deg);
    -ms-transform: rotate(0deg);
    -o-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(360deg);
    -moz-transform: rotate(360deg);
    -ms-transform: rotate(360deg);
    -o-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}
@-moz-keyframes spinner {
  0% {
    -webkit-transform: rotate(0deg);
    -moz-transform: rotate(0deg);
    -ms-transform: rotate(0deg);
    -o-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(360deg);
    -moz-transform: rotate(360deg);
    -ms-transform: rotate(360deg);
    -o-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}
@-o-keyframes spinner {
  0% {
    -webkit-transform: rotate(0deg);
    -moz-transform: rotate(0deg);
    -ms-transform: rotate(0deg);
    -o-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(360deg);
    -moz-transform: rotate(360deg);
    -ms-transform: rotate(360deg);
    -o-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}
@keyframes spinner {
  0% {
    -webkit-transform: rotate(0deg);
    -moz-transform: rotate(0deg);
    -ms-transform: rotate(0deg);
    -o-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(360deg);
    -moz-transform: rotate(360deg);
    -ms-transform: rotate(360deg);
    -o-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}
</style>