<template>
    <div class="row g-0">

        <Sidebar />

        
        <div class="col-sm-8 col-md-9 col-lg-10" id="table-parent">
            <div class="container mt-3">          
                <table class="table table-hover" id="table">
                    <thead>
                        <tr>
                            <th>سرتیتر خبر</th>
                            <th>نوشته شده توسط</th>
                            <th>وضعیت</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="n in news">
                            <td>
                                <router-link v-if="n.status == 'p'" :to="`/news/${n.slug}`" target="_blank">{{n.title}}</router-link>
                                <router-link v-if="n.status == 'd'" :to="`/author-panel/add-news/${n.slug}`">{{n.title}}</router-link>
                                <span v-if="n.status == 's'">{{n.title}}</span>
                            </td>
                            <td><router-link :to="`/user/${n.written_by_username}`">{{n.written_by}}</router-link></td>
                            <td>
                                <span v-if="n.status == 'p'" class="badge bg-success rounded">منتشر شده</span>
                                <span v-if="n.status == 'd'" class="badge bg-danger rounded">پیش نویس</span>
                                <span v-if="n.status == 's'" class="badge bg-info rounded">ارسال به ادمین</span>
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
    components: { Sidebar },
    setup() {
        const store = useStore();
        const route = useRoute();
        const router = useRouter();
        let news = ref("");
        function getData() {
            axios
                .get("ShowNewsPanel/")
                .then(response => {
                news.value = response.data.data;
            })
                .catch(error => {
                console.log(error.response);
            });
        }
        getData();
        return {
            news,
            getData
        };
    },
}
</script>


<style>

</style>