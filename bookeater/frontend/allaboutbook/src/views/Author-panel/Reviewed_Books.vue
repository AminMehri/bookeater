<template>
    <div class="row g-0">

        <Sidebar />


        <div class="col-sm-8 col-md-9 col-lg-10" id="table-parent">
            <div class="container mt-3">          
                <table class="table table-hover">
                    <thead>
                        <tr>
                            <th>نام</th>
                            <th>نویسنده کتاب</th>
                            <th>دسته بندی</th>
                            <th>نقد کننده</th>
                            <th>وضعیت</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="book in reviewedBooks">
                            <td>
                                <router-link v-if="book.status == 'p'" :to="`/reviewed-book/${book.slug}`" target="_blank">{{book.title}}</router-link>
                                <router-link v-if="book.status == 'd'" :to="`/author-panel/add-reviewed-book/${book.slug}`">{{book.title}}</router-link>
                                <span v-if="book.status == 's'">{{book.title}}</span>
                            </td>
                            <td>
                                <span v-for="author in book.author">{{author[0]}}, </span>
                            </td>
                            <td>
                                <span v-for="category in book.category">{{category[0]}}, </span>    
                            </td>
                            <td><router-link :to="`/user/${book.critic_username}`">{{book.critic}}</router-link></td>
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
import { onMounted, ref } from "vue";
import { useStore } from 'vuex'
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'
import Swal from 'sweetalert2'
import Sidebar from "@/components/Sidebar.vue";

export default{
    setup() {
        const store = useStore();
        const route = useRoute();
        const router = useRouter();
        let reviewedBooks = ref("");
        function getData() {
            axios
                .get("ShowReviewedBooksPanel/")
                .then(response => {
                reviewedBooks.value = response.data.data;
            })
                .catch(error => {
                console.log(error.response);
            });
        }
        getData();
        return {
            reviewedBooks,
            getData
        };
    },
    components: { Sidebar }
}
</script>