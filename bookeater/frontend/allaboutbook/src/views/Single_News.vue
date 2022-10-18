<template>

    <metainfo>
      <template v-slot:title="{ content }">{{ content }}</template>
    </metainfo>

    <div v-if="!return404" class="container text-center" id="Single_News">
        <h1 class="mt-5">{{news.title}}</h1>
        <div class="row mt-4">
            <div class="col-md-8 mx-auto single-News p-md-4">
                <img @click="largerImage()" :src="`https://api.bookeater.ir/media${news.image}`" class="img-fluid mb-4" id="larger_image" :alt="`${news.title}`" :title="`${news.title}`">

                <p id="content_news" v-html="news.content"></p>

                <p class="h3 text-warning mb-2 mt-5">و بخوانید</p>

                <div class="row g-md-5 g-0 mt-3">

                    <router-link @click="getData(n.slug)" v-for="n in anotherNews" :to="`/news/${n.slug}`" class="col-12 text-end p-sm-2 my-0 card-news">
                        <h5 class="text-danger">{{n.title}}</h5>
                    </router-link>

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

export default {

    setup() {
        const route = useRoute()

        let slug = ref('')

        let news = ref('')
        let anotherNews = ref('')

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
            .post('ShowSingleNews/', {
                slug: slug.value
            })
            .then(response => {
                news.value = response.data.data[0]
                anotherNews.value = response.data.another_news_data
                return404.value = false
                document.title = news.value.title
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
                let content = ref(document.getElementById('content_news').innerText)
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
            canonical: `https://bookeater.ir/news/${route.params.slug}`,
            'og:type': `${route.params.slug}-bookeater`,
            'og:title': "bookeater",
            'og:site_name': "کتاب خوار",
            'og:url': `https://bookeater.ir/news/${route.params.slug}`,
            'og:image': "https://bookeater.ir/media/image.jpg",
            'twitter:title': "کتاب خوار",
            'twitter:description': "کتاب هایی با بیشترین نمره را در سایت کتاب خوار گرفته اند. شما نیز میتوانید یکی از رای دهندگان به این کتاب باشید.",
            'twitter:site': "https://twitter.com/aminem_mehri",
            'twitter:card': "Summary Card",
            'twitter:image': "https://bookeater.ir/media/image.jpg",
        });

        return {
            largerImage,
            news,
            anotherNews,
            return404,
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