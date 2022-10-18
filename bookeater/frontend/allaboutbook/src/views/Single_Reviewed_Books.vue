<template>

    <metainfo>
      <template v-slot:title="{ content }">{{ content }}</template>
    </metainfo>

    <div v-if="!return404" class="container text-center" id="Single_Category">
        <h1 class="mt-5">{{reviewedBook.title}}</h1>
        <router-link v-for="author in reviewedBook.author" :to="`/author/${author[1]}`" class="text-muted d-block">{{author[0]}}</router-link>
        <div class="row mt-4">
            <div class="col-md-8 mx-auto single-category p-md-4">
                <img @click="largerImage()" :src="`https://api.bookeater.ir/media${reviewedBook.image}`" class="img-fluid mb-4" id="larger_image" :alt="`${reviewedBook.title}`" :title="`${reviewedBook.title}`">

                <p id="content_book" v-html="reviewedBook.content"></p>

                <p>
                    به قلم:<router-link :to="`/user/${reviewedBook.critic_username}`" class="text-danger d-block h4">{{reviewedBook.critic}}</router-link>
                </p>

                <p class="h4 text-warning mb-2 mt-5">نقد های مرتبط</p>

                <div class="text-end">
                    <router-link @click="getData(a.slug)" v-for="a in relatedReviewedBooks" class="d-block text-danger h5" :to="`/reviewed-book/${a.slug}`">{{a.title}}</router-link>
                </div>

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

// Import Swiper Vue.js components
import { Swiper, SwiperSlide } from 'swiper/vue';

// Import Swiper styles
import 'swiper/css';
import 'swiper/css/navigation';

export default {
    components: {
        Swiper,
        SwiperSlide,
    },

    setup() {        
        const route = useRoute()

        let slug = ref('')
        
        let reviewedBook = ref('')

        let relatedReviewedBooks = ref('')

        let return404 = ref(false)

        function getData(sl){
            document.body.scrollTop = 0; // For Safari
            document.documentElement.scrollTop = 0;
            if(sl){
                slug.value = sl
            }else {
                slug.value = route.params.slug
            }

            axios
            .post('ShowSingleReviewedBook/', {
                slug: slug.value
            })
            .then(response => {
                reviewedBook.value = response.data.reviewed_books_data[0]
                relatedReviewedBooks.value = response.data.related_reviewed_data
                document.title = 'نقد و بررسی کتاب ' + reviewedBook.value.title
                return404.value = false
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
                let content = ref(document.getElementById('content_book').innerText)
                content.value = content.value.substring(0,200)
                content.value = content.value.replace(/(\r\n|\n|\r)/gm, "");
                document.querySelector('meta[name="description"]').setAttribute("content", content.value);
                document.querySelector('meta[name="og:description"]').setAttribute("content", content.value);
            }
        })

        function largerImage(){
            var wholePage = document.getElementById('Single_Category')
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
            canonical: `https://bookeater.ir/reviewed-book/${route.params.slug}`,
            'og:type': `${route.params.slug}-bookeater`,
            'og:title': "bookeater",
            'og:site_name': "کتاب خوار",
            'og:url': `https://bookeater.ir/reviewed-book/${route.params.slug}`,
            'og:image': "https://bookeater.ir/media/image.jpg",
            'twitter:title': "کتاب خوار",
            'twitter:description': "کتاب هایی با بیشترین نمره را در سایت کتاب خوار گرفته اند. شما نیز میتوانید یکی از رای دهندگان به این کتاب باشید.",
            'twitter:site': "https://twitter.com/aminem_mehri",
            'twitter:card': "Summary Card",
            'twitter:image': "https://bookeater.ir/media/image.jpg",
        });



        return {
            largerImage,
            reviewedBook,
            relatedReviewedBooks,
            return404,
            getData,
        };
    },
};
</script>


<style scoped>
.single-category{
    border-left: 1px solid rgb(151, 151, 151);
    border-right: 1px solid rgb(151, 151, 151);
    background-color: #eee;
}

#larger_image:hover{
    cursor: all-scroll;
}
</style>