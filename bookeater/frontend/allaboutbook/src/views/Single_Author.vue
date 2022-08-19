<template>
    <div class="container text-center">
        <h1 class="mt-5">{{author.full_name}}</h1>
        <div class="row mt-4">
            <div class="col-md-8 mx-auto single-author p-md-4">
                <img @click="largerImage()" :src="`http://127.0.0.1:8000/media${author.image}`" class="img-fluid mb-4" id="larger_image">

                <p v-html="author.content"></p>

                <p class="h3 text-warning mb-2 mt-5">کتاب های نویسنده</p>

                <section class="container mt-5">
                    <div class="row d-flex">
                        
                            <div v-for="book in relatedBooks" class="col-md-3 col-sm-4 col-6 text-center mb-3">
                                <router-link :to="`/book/${book.slug}`" class="text-decoration-none">
                                    <img class="rounded-circle mb-2 w-100" :src="`http://127.0.0.1:8000/media${book.thumbnail}`" width="200px">
                                    <strong class="text-warning d-block h5">{{book.title}}</strong>
                                </router-link>
                                
                                <p></p>
                            </div>

                    </div>

                </section>
            </div>
        </div>
    </div>
</template>


<script>
import { ref } from "vue";
import { useRoute } from 'vue-router'
import axios from 'axios'

export default {
    setup() {
        const route = useRoute()

        let slug = ref('')
        slug.value = route.params.slug

        let author = ref('')

        let relatedBooks = ref('')

        function getData(){
            document.body.scrollTop = 0; // For Safari
            document.documentElement.scrollTop = 0;
            axios
            .post('ShowSingleAuthor/', {
                slug: slug.value
            })
            .then(response => {
                author.value = response.data.author_data[0]
                relatedBooks.value = response.data.books_data
            })
            .catch(error => {
                console.log(error.response);
            })
        }
        getData()

        function largerImage(){
            var targetImage = document.getElementById('larger_image')
            
            if(screen.width >= 900){
                if(targetImage.style.transform == "scale(1.5)"){
                    targetImage.style.transform = "scale(1)";
                }else{
                    targetImage.style.transform = "scale(1.5)"
                }
            }
            
            targetImage.style.transitionDuration = '0.3s';
        }



        return {
            largerImage,
            author,
            relatedBooks,
            getData,
        };
    },
};
</script>


<style scoped>
.single-author{
    border-left: 1px solid rgb(151, 151, 151);
    border-right: 1px solid rgb(151, 151, 151);
    background-color: #eee;
}

#larger_image:hover{
    cursor: all-scroll;
}
</style>