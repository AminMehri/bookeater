<template>

    <metainfo>
      <template v-slot:title="{ content }">{{ content }}</template>
    </metainfo>

    <div class="row mt-3 g-0">
        <div class="col-3">
            <sidebar class="card ">
                <div class="p-md-4 py-4 fw-bold sidebar">
                    <router-link to="/best-books">
                        <span class="d-block best_tag">برترین ها</span>
                    </router-link>
                    <router-link to="/most-rated-books"> 
                        <span class="most_rated_tag">پربازدید ترین ها</span>
                    </router-link>
                </div>
            </sidebar>
        </div>

        <!-- Modal star rating book -->
        <div class="modal fade w-100" id="staticBackdrop" tabindex="-1">
            <div class="modal-dialog modal-dialog-centered">
                <div class="modal-content bg-dark p-sm-3 p-0">
                    <div class="modal-body mx-auto text-center">
                        <div class="mx-auto star-rating text-white fs-4">
                            <span @click="sendRate(1)" class="fa fa-star"></span>
                            <span @click="sendRate(2)" class="fa fa-star"></span>
                            <span @click="sendRate(3)" class="fa fa-star"></span>
                            <span @click="sendRate(4)" class="fa fa-star"></span>
                            <span @click="sendRate(5)" class="fa fa-star"></span>
                            <span @click="sendRate(6)" class="fa fa-star"></span>
                            <span @click="sendRate(7)" class="fa fa-star"></span>
                            <span @click="sendRate(8)" class="fa fa-star"></span>
                            <span @click="sendRate(9)" class="fa fa-star"></span>
                            <span @click="sendRate(10)" class="fa fa-star"></span>
                        </div>
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal" id="close-modal" hidden>Close</button>
                    </div>
                </div>
            </div>
        </div>

        <div class="col-9">

            <div class="row g-0">
                <div v-for="book in books" class="col-md-4 col-sm-6 position-relative">
                    <span @click="addOrRemoveFromReadlist(book.slug)" v-if="book.in_readlist" class="readlist-cursor position-absolute" style="top: 0rem; left: 0rem; z-index: 5;"><svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" fill="currentColor" class="bi bi-bookmark-plus-fill" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M2 15.5V2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v13.5a.5.5 0 0 1-.74.439L8 13.069l-5.26 2.87A.5.5 0 0 1 2 15.5zm6.5-11a.5.5 0 0 0-1 0V6H6a.5.5 0 0 0 0 1h1.5v1.5a.5.5 0 0 0 1 0V7H10a.5.5 0 0 0 0-1H8.5V4.5z"/></svg></span>
					<span @click="addOrRemoveFromReadlist(book.slug)" v-if="!book.in_readlist" class="readlist-cursor position-absolute" style="top: 0rem; left: 0rem; z-index: 5;"><svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" fill="currentColor" class="bi bi-bookmark-plus" viewBox="0 0 16 16"><path d="M2 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v13.5a.5.5 0 0 1-.777.416L8 13.101l-5.223 2.815A.5.5 0 0 1 2 15.5V2zm2-1a1 1 0 0 0-1 1v12.566l4.723-2.482a.5.5 0 0 1 .554 0L13 14.566V2a1 1 0 0 0-1-1H4z"/><path d="M8 4a.5.5 0 0 1 .5.5V6H10a.5.5 0 0 1 0 1H8.5v1.5a.5.5 0 0 1-1 0V7H6a.5.5 0 0 1 0-1h1.5V4.5A.5.5 0 0 1 8 4z"/></svg></span>

                    <router-link :to="`/book/${book.slug}`" class="text-dark">
                        <div class="card card-book">
                            <img :src="`https://api.bookeater.ir/media${book.thumbnail}`" class="card-img-top img-fluid img-thumbnail" :alt="`${book.title}`" :title="`${book.title}`">
                            <div class="card-body">
                                <div class="card-title">{{book.title}}</div>
                                <span class="fw-bold ms-1">{{book.user_score}}</span>
								<a @click="takeSlug(book.slug)" href="#" class="ms-4 fa fa-star" data-bs-toggle="modal" data-bs-target="#staticBackdrop"></a>
                                <span class="text-muted">({{book.rates}})</span>
								<span class="fa fa-star checked"></span>
								<span class="fw-bold">{{book.score}}</span>
                                <div v-html="book.description" class="card-text"></div>
                            </div>
                        </div>
                    </router-link>

                </div>

            </div>
            

        </div>
    </div>

</template>


<script>
import { ref } from "vue";
import { useRouter } from 'vue-router'
import axios from 'axios'
import { useMeta } from 'vue-meta'

export default {
    setup() {
        useMeta({
            title: "بهترین کتاب ها | کتاب خوار",
            description: "کتاب هایی با بیشترین نمره را در سایت کتاب خوار گرفته اند. شما نیز میتوانید یکی از رای دهندگان به این کتاب باشید.",
            robots: "index, follow",
            keywords: "کتاب خوار, کتاب, نویسنده, نقد کتاب, کتابخانه, دسته بندی های کتاب, برترین کتاب ها",
            googlebot: "index, follow",
            author: "امین مهری",
            owner: "امین مهری",
            canonical: "https://bookeater.ir/best-books",
            'og:type': "best-books-bookeater",
            'og:title': "bookeater",
            'og:description': "کتاب هایی با بیشترین نمره را در سایت کتاب خوار گرفته اند. شما نیز میتوانید یکی از رای دهندگان به این کتاب باشید.",
            'og:site_name': "کتاب خوار|برترین کتاب ها",
            'og:url': "https://bookeater.ir/best-books",
            'og:image': "https://bookeater.ir/media/image.jpg",
            'twitter:title': "کتاب خوار|برترین کتاب ها",
            'twitter:description': "کتاب هایی با بیشترین نمره را در سایت کتاب خوار گرفته اند. شما نیز میتوانید یکی از رای دهندگان به این کتاب باشید.",
            'twitter:site': "https://twitter.com/aminem_mehri",
            'twitter:card': "Summary Card",
            'twitter:image': "https://bookeater.ir/media/image.jpg",
        });

        const router = useRouter()

        let books = ref('')

        let slugForRate = ref('')

        let rate_number = ref('')

        function getData(){
            document.body.scrollTop = 0; // For Safari
            document.documentElement.scrollTop = 0;
            axios
            .get('ShowBestBooks/')
            .then(response => {
                books.value = response.data.data
            })
            .catch(error => {
                console.log(error.response);
            })
        }
        getData()

        // take the book slug that user want to rate it
        function takeSlug(sl){
            slugForRate.value = sl
        }

        // making rate
        function sendRate(number, sl){
            rate_number.value = number

			axios
			.post('MakeRate/', {
				user_score: rate_number.value,
				slug: slugForRate.value
			})
			.then(response => {
				let target = ref(books.value.filter((r) => r.slug == slugForRate.value))
                target.value[0].user_score = rate_number.value
			})
			.catch(error => {
				if(error.response.status == 401){
					router.push('/login')
				}
			})

            document.getElementById('close-modal').click()

        }

        function addOrRemoveFromReadlist(sl){
			axios
			.post('AddOrRemoveFromReadlist/', {
				'slug': sl
			})
			.then(response => {
				let target = ref(books.value.filter((r) => r.slug == sl))
                target.value[0].in_readlist = !target.value[0].in_readlist
			})
			.catch(error => {
				if(error.response.status == 401){
					router.push('/login')
				}
				console.log(error.response);
			})
		}


        return {
            books,
            getData,
            takeSlug,
            sendRate,
            addOrRemoveFromReadlist,
        };
    },
};
</script>



<style scoped>
.checked{
    color: orange;
}

.sidebar{
    background-color: aliceblue;
}

.card-book:hover{
    box-shadow: rgba(0, 0, 0, 0.24) 5px 5px 15px 10px;
    transition-duration: 0.25s;
}

@media screen and (max-width: 806px) {
	.best_tag{
		font-size: 10px !important;
	}
	.most_rated_tag{
		font-size: 10px !important;
	}
}

.router-link-active{
    color: black !important;
}

</style>