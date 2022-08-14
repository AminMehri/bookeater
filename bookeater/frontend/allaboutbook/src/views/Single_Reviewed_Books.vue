<template>
    <div class="container text-center" id="Single_Category">
        <h1 class="mt-5">{{reviewedBook.title}}</h1>
        <router-link v-for="author in reviewedBook.author" :to="`/author/${author[1]}`" class="text-muted d-block">{{author[0]}}</router-link>
        <div class="row mt-4">
            <div class="col-md-8 mx-auto single-category p-5">
                <img @click="largerImage()" :src="`http://127.0.0.1:8000/media${reviewedBook.image}`" class="img-fluid" id="larger_image">

                <p>{{reviewedBook.content}}</p>

                <p>
                    به قلم:<router-link :to="`/user/${reviewedBook.critic_username}`" class="text-danger d-block h4">{{reviewedBook.critic}}</router-link>
                </p>

                <p class="h4 text-warning mb-0 mt-5">نقد های مرتبط</p>

                <div class="text-end">
                    <router-link @click="getData(a.slug)" v-for="a in relatedReviewedBooks" class="d-block text-danger h5" :to="`/reviewed-book/${a.slug}`">{{a.title}}</router-link>
                </div>

            </div>
        </div>
    </div>
</template>


<script>
import { onMounted, watch, ref } from "vue";
import { useStore } from 'vuex'
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'
import Swal from 'sweetalert2'

import { Navigation, A11y } from 'swiper';
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
        const store = useStore()
        const route = useRoute()
        const router = useRouter()

        let slug = ref('')
        

        let reviewedBook = ref('')

        let relatedReviewedBooks = ref('')

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
            })
            .catch(error => {
                console.log(error.response);
            })
        }
        getData()

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



        return {
            modules: [Navigation, A11y],
            largerImage,
            reviewedBook,
            relatedReviewedBooks,
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