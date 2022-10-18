<template>

    <metainfo>
      <template v-slot:title="{ content }">{{ content }}</template>
    </metainfo>
    
    <div class="row g-0">
        <div class="col-lg-8 col-md-9 col-sm-10 mx-auto mt-3">

            <router-link v-for="category in categories" :to="`/category/${category.slug}`">
                <div class="card p-md-4 text-dark">
                    <div class="row g-0" id="category-card">
                        <div class="col-md-4">
                            <img :src="`https://api.bookeater.ir/media${category.thumbnail}`" class="img-fluid rounded-start" :alt="`${category.title}`" :title="`${category.title}`">
                        </div>
                        <div class="col-md-8">
                            <div class="card-body">
                                <h4 class="card-title">{{category.title}}</h4>
                                <p v-html="category.description" class="card-text"></p>

                                <router-link v-for="author in category.related_author" :to="`/author/${author[1]}`"><div class="badge bg-info mx-1">{{author[0]}}</div></router-link>

                            </div>
                        </div>
                    </div>
                </div>
            </router-link>

        </div>
    </div>
</template>


<script>
import { ref } from "vue";
import axios from 'axios'
import { useMeta } from 'vue-meta'

export default {
    setup() {
        useMeta({
            title: "دسته بندی های کتاب | کتاب خوار",
            description: "اطلاعاتی درباره تمام دسته بندی هایی در حوزه کتاب وجود دارند. شما میتوانید اطلاعات کامل هر یک از دسته بندی ها را در صفحه مخصوص دسته بندی مشاهده کنید.",
            robots: "index, follow",
            keywords: "کتاب خوار, کتاب, نویسنده, نقد کتاب, کتابخانه, دسته بندی های کتاب",
            googlebot: "index, follow",
            author: "امین مهری",
            owner: "امین مهری",
            canonical: "https://bookeater.ir/categories",
            'og:type': "categories-bookeater",
            'og:title': "bookeater",
            'og:description': "اطلاعاتی درباره تمام دسته بندی هایی در حوزه کتاب وجود دارند. شما میتوانید اطلاعات کامل هر یک از دسته بندی ها را در صفحه مخصوص دسته بندی مشاهده کنید.",
            'og:site_name': "کتاب خوار|نویسندگان",
            'og:url': "https://bookeater.ir/categories",
            'og:image': "https://bookeater.ir/media/image.jpg",
            'twitter:title': "کتاب خوار|نویسندگان",
            'twitter:description': "اطلاعاتی درباره تمام دسته بندی هایی در حوزه کتاب وجود دارند. شما میتوانید اطلاعات کامل هر یک از دسته بندی ها را در صفحه مخصوص دسته بندی مشاهده کنید.",
            'twitter:site': "https://twitter.com/aminem_mehri",
            'twitter:card': "Summary Card",
            'twitter:image': "https://bookeater.ir/media/image.jpg",
        });

        let categories = ref('')

        function getData(){
            document.body.scrollTop = 0; // For Safari
            document.documentElement.scrollTop = 0;
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
        
        
        return{
            categories,
            getData
        }
    }
}
</script>


<style scoped>
.card{
    border: none;
}
#category-card:hover{
    border: 3px;
    box-shadow: rgba(0, 0, 0, 0.24) 5px 5px 15px 10px;
    transition-duration: 0.25s;
}
.badge:hover{
    background-color: blue !important;
    transition-duration: 0.25s;
}
</style>