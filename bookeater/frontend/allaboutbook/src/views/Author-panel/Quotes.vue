<template>
    <div class="row g-0">

        <Sidebar />

        
        <div class="col-sm-8 col-md-9 col-lg-10" id="table-parent">
            <div class="container mt-3">          
                <table class="table table-hover" id="table">
                    <thead>
                        <tr>
                            <th>نویسنده</th>
                            <th>نقل قول</th>
                            <th>نوشته شده توسط</th>
                            <th>وضعیت</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="quote in quotes">
                            <td><span>{{quote.author}}</span></td>
                            <td><span v-html="quote.description"></span></td>
                            <td><router-link :to="`/user/${quote.written_by_username}`">{{quote.written_by}}</router-link></td>
                            <td>
                                <span v-if="quote.status == 'p'" class="badge bg-success rounded">منتشر شده</span>
                                <span v-if="quote.status == 'd'" class="badge bg-danger rounded">پیش نویس</span>
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
import axios from 'axios'
import Sidebar from "@/components/Sidebar.vue";

export default{
    setup() {
        let quotes = ref("");
        function getData() {
            axios
                .get("ShowQuotesPanel/")
                .then(response => {
                quotes.value = response.data.data;
            })
                .catch(error => {
                console.log(error.response);
            });
        }
        getData();
        return {
            quotes,
            getData
        };
    },
    components: { Sidebar }
}
</script>


<style>

</style>