<template>
    <div class="container text-center" id="Single_News">
        <h1 class="mt-5">{{news.title}}</h1>
        <div class="row mt-4">
            <div class="col-md-8 mx-auto single-News p-md-4">
                <img @click="largerImage()" :src="`http://127.0.0.1:8000/media${news.image}`" class="img-fluid mb-4" id="larger_image">

                <p v-html="news.content"></p>

                <p class="h3 text-warning mb-2 mt-5">و بخوانید</p>

                <div class="row g-md-5 g-0 mt-3">

                    <router-link @click="getData(n.slug)" v-for="n in anotherNews" :to="`/news/${n.slug}`" class="col-12 text-end p-sm-2 my-0 card-news">
                        <h5 class="text-danger">{{n.title}}</h5>
                    </router-link>

                </div>

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

        let news = ref('')
        let anotherNews = ref('')

        function getData(sl){
            document.body.scrollTop = 0; // For Safari
            document.documentElement.scrollTop = 0;
            if(sl){
                slug.value = sl
            }else {
                slug.value = route.params.slug
            }

            axios
            .post('ShowSingleNews/', {
                slug: slug.value
            })
            .then(response => {
                news.value = response.data.data[0]
                anotherNews.value = response.data.another_news_data
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
            largerImage,
            news,
            anotherNews,
            getData
        };
    },
};
</script>



<style scoped>
.single-News{
    border-left: 1px solid rgb(151, 151, 151);
    border-right: 1px solid rgb(151, 151, 151);
    background-color: #eee;
}

.card-news:hover{
    background-color: rgb(255, 207, 189);
    transition-duration: 0.25s;
}

#larger_image:hover{
    cursor: all-scroll;
}
</style>