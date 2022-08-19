<template>
    <div class="row g-0">

        <div class="col-sm-4 col-md-3 col-lg-2">
            <sidebar class="d-flex flex-column flex-shrink-0 p-3 text-white bg-dark sidenav">

                <router-link to="/author-panel" class="d-flex align-items-center mb-3 mb-md-0 text-white text-decoration-none">
                    
                    <span class="fs-4">کتاب خوار</span>
                </router-link>
                
                <hr>

                <ul class="nav nav-pills flex-column">

                    <li class="nav-item text-dark">

                        <button class="accordion-button p-2 bg-white text-dark nav-link align-items-center collapsed1" type="button" data-bs-toggle="collapse" data-bs-target="#dashboard-collapse1">
                                کتاب ها
                        </button>
                        <div class="collapse" id="dashboard-collapse1">
                            <ul class="btn-toggle-nav list-unstyled fw-normal pb-1 small">
                                <li><router-link to="/author-panel/books" class=" text-white" >کتاب ها</router-link></li>
                                <li><router-link to="/author-panel/add-book/new-book" class=" text-white" >اضافه کردن</router-link></li>
                            </ul>
                        </div>
                    </li>

                    <li class="nav-item text-dark">

                        <button class="accordion-button p-2 bg-white text-dark nav-link align-items-center  collapsed2" type="button" data-bs-toggle="collapse" data-bs-target="#dashboard-collapse2">
                                نویسنده ها
                        </button>
                        <div class="collapse" id="dashboard-collapse2">
                            <ul class="btn-toggle-nav list-unstyled fw-normal pb-1 small">
                                <li><router-link to="/author-panel/authors" class=" text-white" >نویسنده ها</router-link></li>
                                <li><router-link to="/author-panel/add-author/new-author" class=" text-white" >اضافه کردن</router-link></li>
                            </ul>
                        </div>
                    </li>

                    <li class="nav-item text-dark">

                        <button class="accordion-button p-2 bg-white text-dark nav-link align-items-center  collapsed3" type="button" data-bs-toggle="collapse" data-bs-target="#dashboard-collapse3">
                                دسته بندی ها
                        </button>
                        <div class="collapse" id="dashboard-collapse3">
                            <ul class="btn-toggle-nav list-unstyled fw-normal pb-1 small">
                                <li><router-link to="/author-panel/categories" class=" text-white" >دسته بندی ها</router-link></li>
                                <li><router-link to="/author-panel/add-category/new-category" class=" text-white" >اضافه کردن</router-link></li>
                            </ul>
                        </div>
                    </li>

                    <li class="nav-item text-dark">

                        <button class="accordion-button p-2 bg-white text-dark nav-link align-items-center  collapsed4" type="button" data-bs-toggle="collapse" data-bs-target="#dashboard-collapse4">
                                نقد ها
                        </button>
                        <div class="collapse" id="dashboard-collapse4">
                            <ul class="btn-toggle-nav list-unstyled fw-normal pb-1 small">
                                <li><router-link to="/author-panel/reviewed-books" class=" text-white" >نقد ها</router-link></li>
                                <li><router-link to="/author-panel/add-reviewed-book/new-reviewed-book" class=" text-white" >اضافه کردن</router-link></li>
                            </ul>
                        </div>
                    </li>

                    <li class="nav-item text-dark">

                        <button class="accordion-button p-2 bg-white text-dark nav-link align-items-center  collapsed5" type="button" data-bs-toggle="collapse" data-bs-target="#dashboard-collapse5">
                                خبر ها
                        </button>
                        <div class="collapse" id="dashboard-collapse5">
                            <ul class="btn-toggle-nav list-unstyled fw-normal pb-1 small">
                                <li><router-link to="/author-panel/news" class=" text-white" >خبر ها</router-link></li>
                                <li><router-link to="/author-panel/add-news/new-news" class=" text-white" >اضافه کردن</router-link></li>
                            </ul>
                        </div>
                    </li>

                    <li class="nav-item text-dark">

                        <button class="accordion-button p-2 bg-white text-dark nav-link align-items-center  collapsed6" type="button" data-bs-toggle="collapse" data-bs-target="#dashboard-collapse6">
                                قصار ها
                        </button>
                        <div class="collapse" id="dashboard-collapse6">
                            <ul class="btn-toggle-nav list-unstyled fw-normal pb-1 small">
                                <li><router-link to="/author-panel/quotes" class=" text-white" >قصار ها</router-link></li>
                                <li><router-link to="/author-panel/add-quote" class=" text-white" >اضافه کردن</router-link></li>
                            </ul>
                        </div>
                    </li>

                </ul>
                <hr>
            </sidebar>
        </div>


        <div class="col-sm-8 col-md-9 col-lg-10 p-3 mt-3">
            <h3 class="text-center">اضافه کردن نقد کتاب</h3>
            <div class="row g-3 border p-4">

                <div class="col-md-6">
                    <label for="inputTitle" class="form-label">نام کتاب</label>
                    <input v-model="title" type="text" class="form-control" id="inputTitle">
                </div>

                <div class="col-md-6">
                    <label for="inputSlug" class="form-label">اسلاگ</label>
                    <input v-model="slug" type="text" class="form-control" id="inputSlug">
                </div>

                <div class="col-md-6">
                    <label for="id_author" class="form-label ms-3">نویسنده:</label>
                    <select  v-model="author" name="author" required="" id="id_author" multiple="">

                        <option v-for="author in authors" :value="`${author.id}`">{{author.full_name}}</option>

                    </select>
                </div>

                <div class="col-md-6">
                    <label for="id_category" class="form-label ms-3">دسته بندی:</label>
                    <select v-model="category" name="category" required="" id="id_category" multiple="">

                        <option v-for="category in categories" :value="`${category.id}`">{{category.title}}</option>

                    </select>
                </div>

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

                <div class="col-12">
                    <button @click="sendData()" class="btn btn-primary">ارسال به ادمین</button>
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


export default{
    setup() {
        const store = useStore()
        const route = useRoute()
        const router = useRouter()

        let title= ref()
        let slug= ref()
        let author= ref()
        let category= ref()
        let description= ref()
        let content= ref()

        let authors = ref('')

        let categories = ref('')

        let editor = ClassicEditor

        let slugForEdit = ref(route.params.slug) 

        if(slugForEdit.value == 'new-reviewed-book'){
            
        }else {
            axios
            .post('ShowSingleReviewedBookEditPanel/', {
                slug: slugForEdit.value
            })
            .then(response => {
                title.value = response.data.data[0].title
                slug.value = response.data.data[0].slug
                description.value = response.data.data[0].description
                content.value = response.data.data[0].content
            })
            .catch(error => {
                if(error.response.status == 400 || error.response.status == 404){
                    Swal.fire({
                        icon: 'warning',
                        title: 'نقدی با این اسلاگ وجود ندارد',
                        backdrop: false,
                        timer: 2500,
                        showConfirmButton: false,
                    })
                    router.push('/author-panel')
                }
                if(error.response.status == 406){
                    Swal.fire({
                        icon: 'warning',
                        title: 'شما قادر به ادیت این نقد نیستید',
                        backdrop: false,
                        timer: 2500,
                        showConfirmButton: false,
                    })
                    router.push('/author-panel')
                }
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
            let formData = new FormData()
            let thumbnailPic = document.getElementById('inputThumbnail')
            let imagePic = document.getElementById('inputImage')

            formData.append('title', title.value)
            formData.append('slug', slug.value)
            formData.append('author', author.value)
            formData.append('category', category.value)
            formData.append('description', description.value)
            formData.append('content', content.value)
            formData.append('thumbnail', thumbnailPic.files[0])
            formData.append('image', imagePic.files[0])

            axios
            .post('AddReviewedBookPanel/', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            })
            .then(response => {
                title.value = ''
                slug.value = ''
                description.value = ''
                content.value = ''

                Swal.fire({
                    icon: 'success',
                    title: 'ثبت نقد کتاب موفقیت انجام شد.',
                    backdrop: false,
                    timer: 1500,
                    showConfirmButton: false,
                    position: 'top',
                })

                router.push('/author-panel/reviewed-books')
            })
            .catch(error => {
                if(error.response.status == 406){
                    Swal.fire({
                    icon: 'warning',
                    title: 'نقد کتاب با این اسلاگ موجود است',
                    backdrop: false,
                    timer: 2500,
                    showConfirmButton: false,
                })
                }
            })
        }
        
        return{
            title,
            slug,
            author,
            category,
            description,
            content,
            authors,
            categories,
            editor,
            getData,
            sendData,
        }
    }
}
</script>