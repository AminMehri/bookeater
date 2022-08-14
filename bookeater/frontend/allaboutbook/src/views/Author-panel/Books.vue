<template>
    <div class="row g-0">

        <div class="col-sm-4 col-md-3 col-lg-2">
            <sidebar class="d-flex flex-column flex-shrink-0 p-3 text-white bg-dark sidenav">

                <a href="/" class="d-flex align-items-center mb-3 mb-md-0 text-white text-decoration-none">
                    
                    <span class="fs-4">کتاب خوار</span>
                </a>
                
                <hr>

                <ul class="nav nav-pills flex-column">

                    <li class="nav-item text-dark">

                        <button class="accordion-button p-2 bg-white text-dark nav-link align-items-center collapsed1" type="button" data-bs-toggle="collapse" data-bs-target="#dashboard-collapse1">
                                کتاب ها
                        </button>
                        <div class="collapse" id="dashboard-collapse1">
                            <ul class="btn-toggle-nav list-unstyled fw-normal pb-1 small">
                                <li><router-link to="/author-panel/books" class=" text-white" >کتاب ها</router-link></li>
                                <li><router-link to="/author-panel/add-book" class=" text-white" >اضافه کردن</router-link></li>
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
                                <li><router-link to="/author-panel/add-author" class=" text-white" >اضافه کردن</router-link></li>
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
                                <li><router-link to="/author-panel/add-category" class=" text-white" >اضافه کردن</router-link></li>
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
                                <li><router-link to="/author-panel/add-reviewed-book" class=" text-white" >اضافه کردن</router-link></li>
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
                                <li><router-link to="/author-panel/add-news" class=" text-white" >اضافه کردن</router-link></li>
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

        
        <div class="col-sm-8 col-md-9 col-lg-10">
            <div class="container mt-3">          
                <table class="table table-hover" id="table">
                    <thead>
                        <tr>
                            <th>نام</th>
                            <th>نویسنده</th>
                            <th>دسته بندی</th>
                            <th>نمره</th>
                            <th>بازدید ها</th>
                            <th>وضعیت</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="book in books">
                            <td><router-link to="/">{{book.title}}</router-link></td>
                            <td>
                                <span v-for="author in book.author">{{author}}, </span>
                            </td>
                            <td>
                                <span v-for="category in book.category">{{category}}, </span>
                            </td>
                            <td>{{book.score}}</td>
                            <td>{{book.rates}}</td>
                            <td>
                                <span v-if="book.status == 'p'" class="badge bg-success rounded">منتشر شده</span>
                                <span v-if="book.status == 'd'" class="badge bg-danger rounded">پیش نویس</span>
                            </td>

                        </tr>
                    </tbody>
                </table>
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

        let books = ref('')

        function getData(){
            axios
			.get('ShowBooksPanel/')
			.then(response => {
				books.value = response.data.data
			})
			.catch(error => {
				console.log(error.response);
			})
        }
        getData()
        
        return{
            books,
            getData
        }
    }
}
</script>


<style>

</style>