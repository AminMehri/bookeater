<template>

    <metainfo>
      <template v-slot:title="{ content }">{{ content }}</template>
    </metainfo>

    <div class="row g-0">
        <div class="col-lg-8 col-md-9 col-sm-10 mx-auto mt-3">

            <router-link v-for="book in books" :to="`/reviewed-book/${book.slug}`">
                <div class="card p-md-4 text-dark">
                    <div class="row g-0" id="category-card">
                        <div class="col-md-4">
                            <img :src="`https://api.bookeater.ir/media${book.thumbnail}`" class="img-fluid rounded w-100" width="200px" :alt="`${book.title}`" :title="`${book.title}`">
                        </div>
                        <div class="col-md-8">
                            <div class="card-body">

                                <h4 class="card-title">نقد و بررسی کتاب {{book.title}}</h4>

                                <router-link v-for="author in book.author" :to="`/author/${author[1]}`"><div class="badge bg-dark fs-6 mx-1">{{author[0]}}</div></router-link>

                                <p v-html="book.description" class="card-text"></p>
                                
                                <router-link v-for="category in book.category" :to="`/category/${category[1]}`"><div class="badge bg-info mx-1">{{category[0]}}</div></router-link>
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
            title: "نقد کتاب | کتاب خوار",
            description: "نقد و بررسی کتاب ها در کتاب خوار, از زیر و بم کتابی که میخوانید باخبر باشید.",
            robots: "index, follow",
            keywords: "کتاب خوار, کتاب, نویسنده, نقد کتاب, کتابخانه, دسته بندی های کتاب",
            googlebot: "index, follow",
            author: "امین مهری",
            owner: "امین مهری",
            canonical: "https://bookeater.ir/reviewed-books",
            'og:type': "reviewed-books-bookeater",
            'og:title': "bookeater",
            'og:description': "نقد و بررسی کتاب ها در کتاب خوار, از زیر و بم کتابی که میخوانید باخبر باشید.",
            'og:site_name': "کتاب خوار|نقد کتاب",
            'og:url': "https://bookeater.ir/reviewed-books",
            'og:image': "https://bookeater.ir/media/image.jpg",
            'twitter:title': "کتاب خوار|نقد کتاب",
            'twitter:description': "نقد و بررسی کتاب ها در کتاب خوار, از زیر و بم کتابی که میخوانید باخبر باشید.",
            'twitter:site': "https://twitter.com/aminem_mehri",
            'twitter:card': "Summary Card",
            'twitter:image': "https://bookeater.ir/media/image.jpg",
        });

        let books = ref('')

        function getData(){
            document.body.scrollTop = 0; // For Safari
            document.documentElement.scrollTop = 0;
            axios
            .get('ShowAllReviewedBooks/')
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