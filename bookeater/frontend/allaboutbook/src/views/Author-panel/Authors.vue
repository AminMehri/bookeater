<template>
    <div class="row g-0">

        <Sidebar />


        <div class="col-sm-8 col-md-9 col-lg-10" id="table-parent">
            <div class="container mt-3">          
                <table class="table table-hover">
                    <thead>
                        <tr>
                            <th>نام نویسنده</th>
                            <th>نوشته شده توسط</th>
                            <th>وضعیت</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="author in authors">
                            <td>
                                <router-link v-if="author.status == 'p'" :to="`/author/${author.slug}`" target="_blank">{{author.full_name}}</router-link>
                                <router-link v-if="author.status == 'd'" :to="`/author-panel/add-author/${author.slug}`">{{author.full_name}}</router-link>
                                <span v-if="author.status == 's'">{{author.full_name}}</span>
                            </td>
                            <td><router-link :to="`/user/${author.written_by_username}`">{{author.written_by}}</router-link></td>
                            <td>
                                <span v-if="author.status == 'p'" class="badge bg-success rounded">منتشر شده</span>
                                <span v-if="author.status == 'd'" class="badge bg-danger rounded">پیش نویس</span>
                                <span v-if="author.status == 's'" class="badge bg-info rounded">ارسال به ادمین</span>
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

        function getData(){
            axios
            .get('ShowAuthorsPanel/')
            .then(response => {
                authors.value = response.data.data
            })
            .catch(error => {
                console.log(error.response);
            })
        }
        getData()
        
        return{
            authors,
            getData
        }
    }
}
</script>