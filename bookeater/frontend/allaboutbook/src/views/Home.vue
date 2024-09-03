<template>

	<metainfo>
      <template v-slot:title="{ content }">{{ content }}</template>
    </metainfo>

	<div class="Home">
		<div class="row g-0">

			<!-- show news -->
			<div class="col-md-4 bg-dark text-light" id="show-news">

				<div class="alert alert-light text-center h4"><span>جدیدترین خبرها</span></div>

				<InsideLoading v-if="loading"/>

				<router-link v-for="n in news" :to="`/news/${n.slug}`" class="text-light">
					<div class="card-body">
						<h5 class="card-title">{{n.title}}</h5>
					</div>
					<hr>
				</router-link>


				<router-link to="/news" class="btn btn-danger w-100">مشاهده تمام خبرها</router-link>
			</div>


			<!-- slideshow -->
			<div class="col-md-8">
				<div id="carouselExampleCaptions" class="carousel slide" data-bs-ride="carousel">
					<div class="carousel-indicators">
						<button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
						<button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="1" aria-label="Slide 2"></button>
						<button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="2" aria-label="Slide 3"></button>
					</div>

					<div class="carousel-inner">

						<div class="carousel-item active">
							<img src="@/assets/1.jpg" class="d-block w-100" height="500px" alt="" title="">
							<div class="carousel-caption text-dark"></div>
						</div>

						<div class="carousel-item">
							<img src="@/assets/2.jpg" class="d-block w-100" height="500px" alt="" title="">
							<div class="carousel-caption text-dark"></div>
						</div>

						<div class="carousel-item">
							<img src="@/assets/3.jpg" class="d-block w-100" height="500px" alt="" title="">
							<div class="carousel-caption text-dark"></div>
						</div>

					</div>

						<button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
							<span class="carousel-control-prev-icon" aria-hidden="true"></span>
							<span class="visually-hidden">Previous</span>
						</button>

						<button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
							<span class="carousel-control-next-icon" aria-hidden="true"></span>
							<span class="visually-hidden">Next</span>
						</button>

				</div>
			</div>
		</div>


		<!-- show quotes -->
		<div class="row g-0">
			<div class="col-md-5 mx-auto">
				<div class="d-flex mt-5">

					<InsideLoading v-if="loading2"/>
						
					<div class="img-fluid mx-3"><img :src="`https://api.bookeater.ir/media${quotes.thumbnail}`" class="rounded-circle" height="100" width="100" :alt="`${quotes.author}`" :title="`${quotes.author}`"></div>
					
					<div class="text-light">
						<h4>{{quotes.author}}</h4>
						<span v-html="quotes.description"></span>
					</div>

				</div>

			</div>
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


		<!-- show best books -->
		<div class="container-fluid">

			<router-link to="/best-books" class="text-decoration-none" ><p class="h3 text-light warning-on-hover mb-0 mt-5">بهترین کتابها ></p></router-link>

			<swiper
				:modules="modules"
				:breakpoints="swiperOptions.breakpoints"
				:slides-per-column-fill="column"
				navigation
				>

				<InsideLoading v-if="loading3"/>
				
				<swiper-slide v-for="book in bestBooks" class="position-relative">
					<span @click="addOrRemoveFromReadlist(book.slug)" v-if="book.in_readlist" class="readlist-cursor position-absolute" style="top: 0rem; left: 0rem; z-index: 5;"><svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" fill="currentColor" class="bi bi-bookmark-plus-fill" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M2 15.5V2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v13.5a.5.5 0 0 1-.74.439L8 13.069l-5.26 2.87A.5.5 0 0 1 2 15.5zm6.5-11a.5.5 0 0 0-1 0V6H6a.5.5 0 0 0 0 1h1.5v1.5a.5.5 0 0 0 1 0V7H10a.5.5 0 0 0 0-1H8.5V4.5z"/></svg></span>
					<span @click="addOrRemoveFromReadlist(book.slug)" v-if="!book.in_readlist" class="readlist-cursor position-absolute" style="top: 0rem; left: 0rem; z-index: 5;"><svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" fill="currentColor" class="bi bi-bookmark-plus" viewBox="0 0 16 16"><path d="M2 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v13.5a.5.5 0 0 1-.777.416L8 13.101l-5.223 2.815A.5.5 0 0 1 2 15.5V2zm2-1a1 1 0 0 0-1 1v12.566l4.723-2.482a.5.5 0 0 1 .554 0L13 14.566V2a1 1 0 0 0-1-1H4z"/><path d="M8 4a.5.5 0 0 1 .5.5V6H10a.5.5 0 0 1 0 1H8.5v1.5a.5.5 0 0 1-1 0V7H6a.5.5 0 0 1 0-1h1.5V4.5A.5.5 0 0 1 8 4z"/></svg></span>
					<router-link :to="`/book/${book.slug}`">
						<div class="profile-card-2"><img :src="`https://api.bookeater.ir/media${book.thumbnail}`" class="img img-responsive" :alt="`${book.title}`" :title="`${book.title}`">
							<div class="book-name">{{book.title}}</div>
							<div class="mx-auto book-star">
								<span class="fw-bold ms-1">{{book.user_score}}</span>
								<a @click="takeSlug(book.slug)" href="#" class="ms-4 fa fa-star" data-bs-toggle="modal" data-bs-target="#staticBackdrop"></a>
								<span class="fa fa-star checked"></span>
								<span class="fw-bold">{{book.score}}</span>
							</div>
						</div>
					</router-link>
				</swiper-slide>
			
			</swiper>

			
			<!-- most popular category -->
			<p class="h3 text-light warning-on-hover mb-0 mt-5">محبوب ترین دسته بندی ها</p>
			<section class="container my-5">
				<div class="row d-flex">

					<InsideLoading v-if="loading4"/>
					
					<div v-for="a in popularCategories" class="col-lg-3 col-md-3 col-sm-4 col-6 text-center mb-3">
						<router-link :to="`/category/${a.slug}`" class="text-decoration-none">
							<img class="rounded-circle mb-2 w-100 image-hover " :src="`https://api.bookeater.ir/media${a.thumbnail}`" width="200px" :alt="`${a.title}`" :title="`${a.title}`">
							<strong class="text-light d-block h5">{{a.title}}</strong>
						</router-link>
						
						<p></p>
					</div>

				</div>

        	</section>


			<!-- show quotes -->
			<div class="row g-0">
				<div class="col-md-5 mx-auto">
					<div class="d-flex mt-5">

						<InsideLoading v-if="loading2"/>
							
						<div class="img-fluid mx-3"><img :src="`https://api.bookeater.ir/media${quotes2.thumbnail}`" class="rounded-circle" height="100" width="100" :alt="`${quotes2.author}`" :title="`${quotes2.author}`"></div>
						
						<div class="text-light">
							<h4>{{quotes2.author}}</h4>
							<span v-html="quotes2.description"></span>
						</div>

					</div>

				</div>
			</div>


			<!-- show most rated books -->
			<router-link to="/most-rated-books" class="text-decoration-none" ><p class="h3 text-light warning-on-hover mb-0 mt-5">پربازدید ترین کتابها ></p></router-link>
			<swiper
				:modules="modules"
				:breakpoints="swiperOptions.breakpoints"
				navigation
				>

				<InsideLoading v-if="loading5"/>

				<swiper-slide v-for="book in mostRatedBooks" class="position-relative">
					<span @click="addOrRemoveFromReadlist(book.slug)" v-if="book.in_readlist" class="readlist-cursor position-absolute" style="top: 0rem; left: 0rem; z-index: 5;"><svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" fill="currentColor" class="bi bi-bookmark-plus-fill" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M2 15.5V2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v13.5a.5.5 0 0 1-.74.439L8 13.069l-5.26 2.87A.5.5 0 0 1 2 15.5zm6.5-11a.5.5 0 0 0-1 0V6H6a.5.5 0 0 0 0 1h1.5v1.5a.5.5 0 0 0 1 0V7H10a.5.5 0 0 0 0-1H8.5V4.5z"/></svg></span>
					<span @click="addOrRemoveFromReadlist(book.slug)" v-if="!book.in_readlist" class="readlist-cursor position-absolute" style="top: 0rem; left: 0rem; z-index: 5;"><svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" fill="currentColor" class="bi bi-bookmark-plus" viewBox="0 0 16 16"><path d="M2 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v13.5a.5.5 0 0 1-.777.416L8 13.101l-5.223 2.815A.5.5 0 0 1 2 15.5V2zm2-1a1 1 0 0 0-1 1v12.566l4.723-2.482a.5.5 0 0 1 .554 0L13 14.566V2a1 1 0 0 0-1-1H4z"/><path d="M8 4a.5.5 0 0 1 .5.5V6H10a.5.5 0 0 1 0 1H8.5v1.5a.5.5 0 0 1-1 0V7H6a.5.5 0 0 1 0-1h1.5V4.5A.5.5 0 0 1 8 4z"/></svg></span>
					<router-link :to="`/book/${book.slug}`">
						<div class="profile-card-2"><img :src="`https://api.bookeater.ir/media${book.thumbnail}`" class="img img-responsive" :alt="`${book.title}`" :title="`${book.title}`">
							<div class="book-name">{{book.title}}</div>
							<div class="mx-auto book-star">
								<span class="fw-bold ms-1">{{book.user_score}}</span>
								<a @click="takeSlug(book.slug)" href="#" class="ms-4 fa fa-star" data-bs-toggle="modal" data-bs-target="#staticBackdrop"></a>
								<span>({{book.rates}})</span>
								<span class="fa fa-star checked"></span>
								<span class="fw-bold">{{book.score}}</span>
							</div>
						</div>
					</router-link>
				</swiper-slide>
			
			</swiper>


			<!-- most popular authors -->
			<p class="h3 text-light warning-on-hover mb-2 mt-5">محبوب ترین نویسنده ها</p>
			<section class="container mt-5">
				<div class="row d-flex">

					<InsideLoading v-if="loading6"/>
					
					<div v-for="a in popularAuthors" class="col-lg-3 col-md-3 col-sm-4 col-6 text-center mb-3">
						<router-link :to="`/author/${a.slug}`" class="text-decoration-none">
							<img class="rounded-circle mb-2 w-100 image-hover-reverse" :src="`https://api.bookeater.ir/media${a.thumbnail}`" width="200px" :alt="`${a.full_name}`" :title="`${a.full_name}`">
							<strong class="text-light d-block h5">{{a.full_name}}</strong>
						</router-link>
						
						<p></p>
					</div>
					
				</div>

        	</section>

		</div>
	</div>

</template>



<script>
import { ref } from "vue";
import { useRouter } from 'vue-router'
import axios from 'axios'
import { useMeta } from 'vue-meta'
import InsideLoading from '@/components/InsideLoading.vue'

// Import Swiper Vue.js components
import { Swiper, SwiperSlide } from 'swiper/vue';

// Import Swiper styles
import 'swiper/css';
import 'swiper/css/navigation';

export default {
	components: {
		Swiper,
		SwiperSlide,
		InsideLoading,
	},

	setup() {
		useMeta({
            title: "کتاب خوار | نقد, رای, برترین ها و هر آنچه لازم است درباره کتاب بدانید",
            description: "دیدن بهترین و پربازدید ترین و برترین نقد ها در پلتفرم کاربر محور کتاب خوار. با کتاب خوار خوره کتاب باشید",
            robots: "index, follow",
            keywords: "کتاب خوار, کتاب, نویسنده, نقد کتاب, کتابخانه, دسته بندی های کتاب, برترین کتاب ها",
            googlebot: "index, follow",
            author: "امین مهری",
            owner: "امین مهری",
            canonical: "https://bookeater.ir/",
            'og:type': "bookeater",
            'og:title': "bookeater",
            'og:description': "دیدن بهترین و پربازدید ترین و برترین نقد ها در پلتفرم کاربر محور کتاب خوار. با کتاب خوار خوره کتاب باشید",
            'og:site_name': "کتاب خوار",
            'og:url': "https://bookeater.ir/",
            'og:image': "https://bookeater.ir/media/image.jpg",
            'twitter:title': "کتاب خوار | نقد, رای, برترین ها و هر آنچه لازم است درباره کتاب بدانید",
            'twitter:description': "دیدن بهترین و پربازدید ترین و برترین نقد ها در پلتفرم کاربر محور کتاب خوار. با کتاب خوار خوره کتاب باشید",
            'twitter:site': "https://twitter.com/aminem_mehri",
            'twitter:card': "Summary Card",
            'twitter:image': "https://bookeater.ir/media/image.jpg",
        });

		let swiperOptions = {
			breakpoints: {       
				320: {       
					slidesPerView: 1,
				},          
				400: {       
					slidesPerView: 2,       
				},   
			
				650: {       
					slidesPerView: 3,       
				},

				925: {       
					slidesPerView: 4,       
				} 
			}
		}

		const router = useRouter()

		let news = ref('')

		let quotes = ref('')
		let quotes2 = ref('')

		let bestBooks = ref('')

		let popularCategories = ref('')

		let mostRatedBooks = ref('')

		let popularAuthors = ref('')

		let loading = ref(true)
		let loading2 = ref(true)
		let loading3 = ref(true)
		let loading4 = ref(true)
		let loading5 = ref(true)
		let loading6 = ref(true)

		let slugForRate = ref('')

        let rate_number = ref('')

		function getData(){
			document.body.scrollTop = 0; // For Safari
            document.documentElement.scrollTop = 0;
			axios
			.get('ShowAllNews/')
			.then(response => {
				news.value = response.data.data
				if(news.value.length > 5){
					news.value = news.value.slice(0, 5)
				}
				loading.value = false
			})
			.catch(error => {
				console.log(error.response);
			})
			

			axios
			.get('ShowQuotes/')
			.then(response => {
				quotes.value = response.data.data
				quotes2.value = quotes.value[Math.floor(Math.random()*quotes.value.length)]	
				quotes.value = quotes.value[Math.floor(Math.random()*quotes.value.length)]
				loading2.value = false
			})
			.catch(error => {
				console.log(error.response);
			})

			axios
			.get('ShowBestBooks/')
			.then(response => {
				bestBooks.value = response.data.data
				loading3.value = false
			})
			.catch(error => {
				console.log(error.response);
			})
			
			axios
			.get('ShowPopularCategories/')
			.then(response => {
				popularCategories.value = response.data.data
				loading4.value = false
			})
			.catch(error => {
				console.log(error.response);
			})

			axios
			.get('ShowMostRatedBooks/')
			.then(response => {
				mostRatedBooks.value = response.data.data
				loading5.value = false
			})
			.catch(error => {
				console.log(error.response);
			})
			
			axios
			.get('ShowPopularAuthors/')
			.then(response => {
				popularAuthors.value = response.data.data
				loading6.value = false
			})
			.catch(error => {
				console.log(error.response);
			})
		}
		getData()



		function takeSlug(sl){
            slugForRate.value = sl
        }




        function sendRate(number, sl){
            rate_number.value = number

			axios
			.post('MakeRate/', {
				user_score: rate_number.value,
				slug: slugForRate.value
			})
			.then(response => {
				let targetBestBooks = ref(bestBooks.value.filter((r) => r.slug == slugForRate.value))
				let targetMostRatedBooks = ref(mostRatedBooks.value.filter((r) => r.slug == slugForRate.value))
				if(targetBestBooks.value == 0){
					targetMostRatedBooks.value[0].user_score = rate_number.value
				} else if(targetMostRatedBooks.value == 0){
					targetBestBooks.value[0].user_score = rate_number.value
				} else{
					targetMostRatedBooks.value[0].user_score = rate_number.value
					targetBestBooks.value[0].user_score = rate_number.value
				}
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
				let targetBestBooks = ref(bestBooks.value.filter((r) => r.slug == sl))
				let targetMostRatedBooks = ref(mostRatedBooks.value.filter((r) => r.slug == sl))
				if(targetBestBooks.value == 0){
					targetMostRatedBooks.value[0].in_readlist = !targetMostRatedBooks.value[0].in_readlist
				} else if(targetMostRatedBooks.value == 0){
					targetBestBooks.value[0].in_readlist = !targetBestBooks.value[0].in_readlist
				} else{
					targetMostRatedBooks.value[0].in_readlist = !targetMostRatedBooks.value[0].in_readlist
					targetBestBooks.value[0].in_readlist = !targetBestBooks.value[0].in_readlist
				}
			})
			.catch(error => {
				if(error.response.status == 401){
					router.push('/login')
				}
				console.log(error.response);
			})
		}
		


		return {
			news,
			quotes,
			quotes2,
			bestBooks,
			popularCategories,
			mostRatedBooks,
			popularAuthors,
			loading,
			loading2,
			loading3,
			loading4,
			loading5,
			loading6,
			swiperOptions,
			getData,
			takeSlug,
			sendRate,
			addOrRemoveFromReadlist,
		};
	},
};
</script>


<style>

.Home {
	background-color: #000;
}

.swiper {
	width: 100%;
	padding-top: 10px;
	padding-bottom: 10px;
	user-select: none;
}

.swiper-slide {
	background-position: center;
	background-size: cover;
	width: 300px;
	/* height: 300px; */
}

.swiper-slide img {
	display: block;
	width: 100%;
	height: 412px;
}

.swiper-button-prev, .swiper-rtl .swiper-button-next {
	border: 1px solid #ffc107;
    padding: 25px 10px 25px 10px;
	
}

.swiper-button-prev, .swiper-rtl .swiper-button-next:hover {
	color: #ffc107;
}

#show-news{
	height: 500px;
	overflow-y: scroll;
}

#show-news::-webkit-scrollbar {
  width: 10px;
}
 
#show-news::-webkit-scrollbar-thumb {
  background: #666;
  border-radius: 20px;
}

#show-news::-webkit-scrollbar-track {
  background: #ddd;
  border-radius: 20px;
}

#show-news .card-body:hover{
	background-color:#666;
	transition-duration: 0.5s;
}

.warning-on-hover:hover{
	color: #ffc107 !important;
	transition-duration: 0.3s
}


.profile-card-2 {
    max-width: 300px;
    background-color: #FFF;
    box-shadow: 0px 0px 25px rgba(0, 0, 0, 0.1);
    background-position: center;
    overflow: hidden;
    position: relative;
    margin: 10px auto;
    cursor: pointer;
    border-radius: 10px;
}

.profile-card-2 img {
    transition: all linear 0.25s;
}

.profile-card-2 .book-name {
    position: absolute;
    left: 30px;
    bottom: 70px;
    font-size: 30px;
    color: #FFF;
    text-shadow: 0px 0px 20px rgba(0, 0, 0, 0.5);
    font-weight: bold;
    transition: all linear 0.25s;
}

.profile-card-2 .profile-icons {
    position: absolute;
    bottom: 30px;
    right: 30px;
    color: #FFF;
    transition: all linear 0.25s;
}

.profile-card-2 .book-star {
    position: absolute;
    bottom: 40px;
    left: 30px;
    color: #FFF;
    font-size: 20px;
    transition: all linear 0.25s;
}

.profile-card-2:hover img {
    filter: grayscale(100%);
}

.profile-card-2:hover .book-name {
    bottom: 80px;
}

.profile-card-2:hover .book-star {
    bottom: 60px;
}

.profile-card-2:hover .profile-icons {
    right: 40px;
}

.image-hover{
	filter: grayscale(0%);
}

.image-hover:hover{
	filter: grayscale(100%);
	transition-duration: 0.5s;
}

.image-hover-reverse{
	filter: grayscale(100%)
}

.image-hover-reverse:hover{
	filter: grayscale(0%);
	transition-duration: 0.5s;
}

.readlist-cursor{
	cursor: pointer;
}

@media screen and (max-width: 952px) {
	.book-star{
		font-size: 14px !important;
		margin-top: 3rem !important;
	}
	.book-name{
		font-size: 17px !important;
	}
	.swiper-slide img {
		height: 312px;
	}

}

@media screen and (max-width: 700px) {
	.book-star{
		font-size: 15px !important;
		margin-top: 3rem !important;
	}
	.book-name{
		font-size: 15px !important;
	}
	.swiper-button-prev, .swiper-rtl .swiper-button-next {
		visibility: hidden;
		display: none;
	}
}

@media screen and (max-width: 557px) {
	.book-star{
		font-size: 12px !important;
		margin-top: 4rem !important;
	}
	.book-name{
		font-size: 12px !important;
	}
}

.star-rating:hover > span:before {
    color: #ffc107;
}

.star-rating > span:hover ~ span:before {
    color: #c7c5c5;
}

.star-rating > span:hover{
	cursor: pointer;
}


</style>