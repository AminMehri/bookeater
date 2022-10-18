<template>

    <metainfo>
      <template v-slot:title="{ content }">{{ content }}</template>
    </metainfo>

    بارسلونا همچنین امیدوار بود که سزار آسپیلیکوئتا را هم جذب کند ا
</template>


<script>
import { useMeta } from 'vue-meta'

export default {
    setup () {
        useMeta({
            title: "توسعه دهندگان کتاب خوار",
            description: "سایت کتاب محور کتاب خوار نیاز شما را برای هر آنچه که لازم است درباره کتاب اعم از نویسنده آن و دسته بندی اش و همچنین نقد آن بدانید را برآورده میکند. با کتاب خوار خوره کتاب شوید.",
            robots: "index, follow",
            keywords: "کتاب خوار, کتاب, نویسنده, نقد کتاب, کتابخانه",
            googlebot: "index, follow",
            author: "امین مهری",
            owner: "امین مهری",
            canonical: "https://bookeater.ir/developers",
            'og:type': "developers-bookeater",
            'og:title': "bookeater",
            'og:description': "سایت کتاب محور کتاب خوار نیاز شما را برای هر آنچه که لازم است درباره کتاب اعم از نویسنده آن و دسته بندی اش و همچنین نقد آن بدانید را برآورده میکند. با کتاب خوار خوره کتاب شوید.",
            'og:site_name': "کتاب خوار",
            'og:url': "https://bookeater.ir/developers",
            'og:image': "https://bookeater.ir/media/image.jpg",
            'twitter:title': "کتاب خوار",
            'twitter:description': "سایت کتاب محور کتاب خوار نیاز شما را برای هر آنچه که لازم است درباره کتاب اعم از نویسنده آن و دسته بندی اش و همچنین نقد آن بدانید را برآورده میکند. با کتاب خوار خوره کتاب شوید.",
            'twitter:site': "https://twitter.com/aminem_mehri",
            'twitter:card': "Summary Card",
            'twitter:image': "https://bookeater.ir/media/image.jpg",
        });
    }
}
</script>