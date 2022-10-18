<template>
    <div class="row g-0">

        <Sidebar />
        
        <div class="col-sm-8 col-md-9 col-lg-10" id="table-parent">
            <div class="mt-3">          
                <table class="table table-hover" id="table">
                    <thead>
                        <tr>
                            <th>نام کتاب</th>
                            <th>نویسنده</th>
                            <th>دسته بندی</th>
                            <th>نمره</th>
                            <th>بازدید ها</th>
                            <th>نوشته شده توسط</th>
                            <th>وضعیت</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="book in books">
                            <td>
                                <router-link v-if="book.status == 'p'" :to="`/book/${book.slug}`" target="_blank">{{book.title}}</router-link>
                                <router-link v-if="book.status == 'd'" :to="`/author-panel/add-book/${book.slug}`">{{book.title}}</router-link>
                                <span v-if="book.status == 's'">{{book.title}}</span>
                            </td>
                            <td>
                                <span v-for="author in book.author">{{author}}, </span>
                            </td>
                            <td>
                                <span v-for="category in book.category">{{category}}, </span>
                            </td>
                            <td>{{book.score}}</td>
                            <td>{{book.rates}}</td>
                            <td><router-link :to="`/user/${book.written_by_username}`">{{book.written_by}}</router-link></td>
                            <td>
                                <span v-if="book.status == 'p'" class="badge bg-success rounded">منتشر شده</span>
                                <span v-if="book.status == 'd'" class="badge bg-danger rounded">پیش نویس</span>
                                <span v-if="book.status == 's'" class="badge bg-info rounded">ارسال به ادمین</span>
                            </td>

                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        
    </div>
</template>


<script>
import { ref } from "vue";
import { useStore } from 'vuex'
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'
import Swal from 'sweetalert2'
import Sidebar from '@/components/Sidebar.vue'

export default{
    components: {
        Sidebar
    },
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
#table-parent{
    width: 1100px !important;
    overflow-x:scroll;
}
</style>