<template>
    <div class="row g-0">

        <Sidebar />


        <div class="col-sm-8 col-md-9 col-lg-10" id="table-parent">
            <div class="container mt-3">          
                <table class="table table-hover">
                    <thead>
                        <tr>
                            <th>نام دسته بندی</th>
                            <th>نوشته شده توسط</th>
                            <th>وضعیت</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="category in categories">
                            <td>
                                <router-link v-if="category.status == 'p'" :to="`/category/${category.slug}`" target="_blank">{{category.title}}</router-link>
                                <router-link v-if="category.status == 'd'" :to="`/author-panel/add-category/${category.slug}`">{{category.title}}</router-link>
                                <span v-if="category.status == 's'">{{category.title}}</span>
                            </td>
                            <td><router-link :to="`/user/${category.written_by_username}`">{{category.written_by}}</router-link></td>
                            <td>
                                <span v-if="category.status == 'p'" class="badge bg-success rounded">منتشر شده</span>
                                <span v-if="category.status == 'd'" class="badge bg-danger rounded">پیش نویس</span>
                                <span v-if="category.status == 's'" class="badge bg-info rounded">ارسال به ادمین</span>
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

        let categories = ref('')

        function getData(){
            axios
            .get('ShowCategoriesPanel/')
            .then(response => {
                categories.value = response.data.data
            })
            .catch(error => {
                console.log(error.response);
            })
        }
        getData()
        
        return{
            categories,
            getData
        }
    }
}
</script>