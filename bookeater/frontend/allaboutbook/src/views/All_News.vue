<template>

    <metainfo>
      <template v-slot:title="{ content }">{{ content }}</template>
    </metainfo>

    <div class="row g-0 bg-pink">
        <div class="col-md-8 mx-auto">

            <div class="row g-md-5 mt-5 g-0">

                <router-link v-for="n in news" :to="`/news/${n.slug}`" class="col-md-4 col-sm-6 p-md-3 p-3 text-dark card-news">
                    <h5>{{n.title}}</h5>
                    <p v-html="n.description" style="text-align: justify;"></p>
                </router-link>

            </div>

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
            title: "خبر های کتاب | کتاب خوار",
            description: "جدیدترین خبرها در حوزه کتاب. با کتاب خوار از جدید ترین خبر ها درباره کتاب با خبر باشید.",
            robots: "index, follow",
            keywords: "کتاب خوار, کتاب, نویسنده, نقد کتاب, کتابخانه, دسته بندی های کتاب",
            googlebot: "index, follow",
            author: "امین مهری",
            owner: "امین مهری",
            canonical: "https://bookeater.ir/news",
            'og:type': "news-bookeater",
            'og:title': "bookeater",
            'og:description': "جدیدترین خبرها در حوزه کتاب. با کتاب خوار از جدید ترین خبر ها درباره کتاب باخبر باشید.",
            'og:site_name': "کتاب خوار|خبرها",
            'og:url': "https://bookeater.ir/news",
            'og:image': "https://bookeater.ir/media/image.jpg",
            'twitter:title': "کتاب خوار|خبرها",
            'twitter:description': "جدیدترین خبرها در حوزه کتاب. با کتاب خوار از جدید ترین خبر ها درباره کتاب باخبر باشید.",
            'twitter:site': "https://twitter.com/aminem_mehri",
            'twitter:card': "Summary Card",
            'twitter:image': "https://bookeater.ir/media/image.jpg",
        });

        let news = ref('')

        function getData(){
            document.body.scrollTop = 0; // For Safari
            document.documentElement.scrollTop = 0;
            axios
            .get('ShowAllNews/')
            .then(response => {
                news.value = response.data.data
            })
            .catch(error => {
                console.log(error.response);
            })
        }
        getData()
        
        return{
            news,
            getData
        }
    }
}
</script>


<style scoped>
.bg-pink{
    background-color: rgb(250, 226, 230);
}

.card-news:hover{
    background-color: rgb(255, 207, 189);
    transition-duration: 0.25s;
}
</style>