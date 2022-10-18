<template>

    <metainfo>
      <template v-slot:title="{ content }">{{ content }}</template>
    </metainfo>

    <div v-if="!return404" class="container text-center">
        <h1 class="mt-5">{{author.full_name}}</h1>
        <div class="row mt-4">
            <div class="col-md-8 mx-auto single-author p-md-4">
                <img @click="largerImage()" :src="`https://api.bookeater.ir/media${author.image}`" class="img-fluid mb-4" id="larger_image" :alt="`${author.full_name}`" :title="`${author.full_name}`">

                <p id="content_author" v-html="author.content"></p>

                <p class="h3 text-warning mb-2 mt-5">کتاب های نویسنده</p>

                <section class="container mt-5">
                    <div class="row d-flex">
                        
                            <div v-for="book in relatedBooks" class="col-md-3 col-sm-4 col-6 text-center mb-3">
                                <router-link :to="`/book/${book.slug}`" class="text-decoration-none">
                                    <img class="rounded-circle mb-2 w-100" :src="`https://api.bookeater.ir/media${book.thumbnail}`" width="200px" :alt="`${book.title}`" :title="`${book.title}`">
                                    <strong class="text-warning d-block h5">{{book.title}}</strong>
                                </router-link>
                                
                                <p></p>
                            </div>

                    </div>

                </section>
            </div>
        </div>
    </div>

    <div v-if="return404" class="PageNotFound bg-dark">
        <div class="container text-center p-5">
            <h1 class="text-muted" id="text-404">404</h1>
            <p class="text-light">صفحه مورد نظر شما یافت نشد.</p>
            <hr class="text-white">    
        </div>
    </div>
</template>


<script>
import { ref, onMounted } from "vue";
import { useRoute } from 'vue-router'
import axios from 'axios'
import { useMeta } from 'vue-meta'

export default {
    setup() {
        const route = useRoute()

        let slug = ref('')
        slug.value = route.params.slug

        let author = ref('')

        let relatedBooks = ref('')

        let return404 = ref(false)

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
                return404.value = false
                document.title  = author.value.full_name
            })
            .catch(error => {
                return404.value = true
                console.log(error.response);
            })
        }
        getData()

        // meta tags
        onMounted(() => {
            setTimeout(setMetaDescription, 1000)
            function setMetaDescription(){
                let content = ref(document.getElementById('content_author').innerText)
                content.value = content.value.substring(0,200)
                content.value = content.value.replace(/(\r\n|\n|\r)/gm, "");
                document.querySelector('meta[name="description"]').setAttribute("content", content.value);
                document.querySelector('meta[name="og:description"]').setAttribute("content", content.value);
            }
        })

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

        useMeta({
            robots: "index, follow",
            keywords: "کتاب خوار, کتاب, نویسنده, نقد کتاب, کتابخانه, دسته بندی های کتاب, برترین کتاب ها",
            googlebot: "index, follow",
            author: "امین مهری",
            owner: "امین مهری",
            canonical: `https://bookeater.ir/author/${route.params.slug}`,
            'og:type': `${route.params.slug}-bookeater`,
            'og:title': "bookeater",
            'og:site_name': "کتاب خوار",
            'og:url': `https://bookeater.ir/author/${route.params.slug}`,
            'og:image': "https://bookeater.ir/media/image.jpg",
            'twitter:title': "کتاب خوار",
            'twitter:description': "کتاب هایی با بیشترین نمره را در سایت کتاب خوار گرفته اند. شما نیز میتوانید یکی از رای دهندگان به این کتاب باشید.",
            'twitter:site': "https://twitter.com/aminem_mehri",
            'twitter:card': "Summary Card",
            'twitter:image': "https://bookeater.ir/media/image.jpg",
        });


        return {
            largerImage,
            author,
            relatedBooks,
            return404,
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