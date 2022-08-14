<template>

	<div class="Home">
		<div class="row g-0">

			<!-- show news -->
			<div class="col-md-4 bg-dark text-light" id="show-news">

				<div class="alert alert-light text-center h4"><span>جدیدترین خبرها</span></div>

				<svg v-if="loading" class="w-100" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" style="margin: auto; background: rgb(0, 0, 0); display: block;" width="184px" height="184px" viewBox="0 0 100 100" preserveAspectRatio="xMidYMid">
					<path d="M16 50A34 34 0 0 0 84 50A34 37.6 0 0 1 16 50" fill="#ffc200" stroke="none">
					<animateTransform attributeName="transform" type="rotate" dur="0.8695652173913042s" repeatCount="indefinite" keyTimes="0;1" values="0 50 51.8;360 50 51.8"></animateTransform>
					</path>
				</svg>

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
							<img src="https://picsum.photos/800/500" class="d-block w-100" height="500px">
							<div class="carousel-caption text-dark">
								<h5>First slide label</h5>
								<p>Some representative placeholder content for the first slide.</p>
							</div>
						</div>

						<div class="carousel-item">
							<img src="https://picsum.photos/800/500" class="d-block w-100" height="500px">
							<div class="carousel-caption text-dark">
								<h5>Second slide label</h5>
								<p>Some representative placeholder content for the second slide.</p>
							</div>
						</div>

						<div class="carousel-item">
							<img src="https://picsum.photos/800/500" class="d-block w-100" height="500px">
							<div class="carousel-caption text-dark">
								<h5>Third slide label</h5>
								<p>Some representative placeholder content for the third slide.</p>
							</div>
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

					<svg v-if="loading2" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" style="margin: auto; background: rgb(0, 0, 0); display: block;" width="184px" height="184px" viewBox="0 0 100 100" preserveAspectRatio="xMidYMid">
					<path d="M16 50A34 34 0 0 0 84 50A34 37.6 0 0 1 16 50" fill="#ffc200" stroke="none">
					<animateTransform attributeName="transform" type="rotate" dur="0.8695652173913042s" repeatCount="indefinite" keyTimes="0;1" values="0 50 51.8;360 50 51.8"></animateTransform>
					</path>
				</svg>
						
					<div class="img-fluid mx-3"><img :src="`http://127.0.0.1:8000/media${quotes.thumbnail}`" class="rounded-circle" height="100" width="100"></div>
					
					<div class="text-light">
						<h4>{{quotes.author}}</h4>
						<span>{{quotes.description}}</span>
					</div>

				</div>

			</div>
		</div>


		<!-- Modal star rating book -->
		<div class="modal fade w-100" id="staticBackdrop" tabindex="-1">
			<div class="modal-dialog modal-dialog-centered">
				<div class="modal-content bg-dark p-5">
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
				:slides-per-view="4"
				:loop="true"
				:slides-per-column-fill="column"
				navigation
				>

				<svg v-if="loading3" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" style="margin: auto; background: rgb(0, 0, 0); display: block;" width="184px" height="184px" viewBox="0 0 100 100" preserveAspectRatio="xMidYMid">
					<path d="M16 50A34 34 0 0 0 84 50A34 37.6 0 0 1 16 50" fill="#ffc200" stroke="none">
					<animateTransform attributeName="transform" type="rotate" dur="0.8695652173913042s" repeatCount="indefinite" keyTimes="0;1" values="0 50 51.8;360 50 51.8"></animateTransform>
					</path>
				</svg>
				
				<swiper-slide v-for="book in bestBooks" class="position-relative">
					<span @click="addOrRemoveFromReadlist(book.slug)" v-if="book.in_readlist" class="readlist-cursor position-absolute" style="top: 0rem; left: 0rem; z-index: 5;"><svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" fill="currentColor" class="bi bi-bookmark-plus-fill" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M2 15.5V2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v13.5a.5.5 0 0 1-.74.439L8 13.069l-5.26 2.87A.5.5 0 0 1 2 15.5zm6.5-11a.5.5 0 0 0-1 0V6H6a.5.5 0 0 0 0 1h1.5v1.5a.5.5 0 0 0 1 0V7H10a.5.5 0 0 0 0-1H8.5V4.5z"/></svg></span>
					<span @click="addOrRemoveFromReadlist(book.slug)" v-if="!book.in_readlist" class="readlist-cursor position-absolute" style="top: 0rem; left: 0rem; z-index: 5;"><svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" fill="currentColor" class="bi bi-bookmark-plus" viewBox="0 0 16 16"><path d="M2 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v13.5a.5.5 0 0 1-.777.416L8 13.101l-5.223 2.815A.5.5 0 0 1 2 15.5V2zm2-1a1 1 0 0 0-1 1v12.566l4.723-2.482a.5.5 0 0 1 .554 0L13 14.566V2a1 1 0 0 0-1-1H4z"/><path d="M8 4a.5.5 0 0 1 .5.5V6H10a.5.5 0 0 1 0 1H8.5v1.5a.5.5 0 0 1-1 0V7H6a.5.5 0 0 1 0-1h1.5V4.5A.5.5 0 0 1 8 4z"/></svg></span>
					<router-link :to="`/book/${book.slug}`">
						<div class="profile-card-2"><img :src="`http://127.0.0.1:8000/media${book.thumbnail}`" class="img img-responsive">
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

					<svg v-if="loading4" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" style="margin: auto; background: rgb(0, 0, 0); display: block;" width="184px" height="184px" viewBox="0 0 100 100" preserveAspectRatio="xMidYMid">
						<path d="M16 50A34 34 0 0 0 84 50A34 37.6 0 0 1 16 50" fill="#ffc200" stroke="none">
						<animateTransform attributeName="transform" type="rotate" dur="0.8695652173913042s" repeatCount="indefinite" keyTimes="0;1" values="0 50 51.8;360 50 51.8"></animateTransform>
						</path>
					</svg>
					
					<div v-for="a in popularCategories" class="col-lg-3 col-md-3 col-sm-4 text-center mb-3">
						<router-link :to="`/category/${a.slug}`" class="text-decoration-none">
							<img class="rounded-circle mb-2 w-100 image-hover " :src="`http://127.0.0.1:8000/media${a.thumbnail}`" width="200px">
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

						<svg v-if="loading2" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" style="margin: auto; background: rgb(0, 0, 0); display: block;" width="184px" height="184px" viewBox="0 0 100 100" preserveAspectRatio="xMidYMid">
							<path d="M16 50A34 34 0 0 0 84 50A34 37.6 0 0 1 16 50" fill="#ffc200" stroke="none">
							<animateTransform attributeName="transform" type="rotate" dur="0.8695652173913042s" repeatCount="indefinite" keyTimes="0;1" values="0 50 51.8;360 50 51.8"></animateTransform>
							</path>
						</svg>
							
						<div class="img-fluid mx-3"><img :src="`http://127.0.0.1:8000/media${quotes2.thumbnail}`" class="rounded-circle" height="100" width="100"></div>
						
						<div class="text-light">
							<h4>{{quotes2.author}}</h4>
							<span>{{quotes2.description}}</span>
						</div>

					</div>

				</div>
			</div>


			<!-- show most rated books -->
			<router-link to="/most-rated-books" class="text-decoration-none" ><p class="h3 text-light warning-on-hover mb-0 mt-5">پربازدید ترین کتابها ></p></router-link>
			<swiper
				:modules="modules"
				:slides-per-view="4"
				:loop="true"
				navigation
				>

				<svg v-if="loading5" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" style="margin: auto; background: rgb(0, 0, 0); display: block;" width="184px" height="184px" viewBox="0 0 100 100" preserveAspectRatio="xMidYMid">
					<path d="M16 50A34 34 0 0 0 84 50A34 37.6 0 0 1 16 50" fill="#ffc200" stroke="none">
					<animateTransform attributeName="transform" type="rotate" dur="0.8695652173913042s" repeatCount="indefinite" keyTimes="0;1" values="0 50 51.8;360 50 51.8"></animateTransform>
					</path>
				</svg>

				<swiper-slide v-for="book in mostRatedBooks" class="position-relative">
					<span @click="addOrRemoveFromReadlist(book.slug)" v-if="book.in_readlist" class="readlist-cursor position-absolute" style="top: 0rem; left: 0rem; z-index: 5;"><svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" fill="currentColor" class="bi bi-bookmark-plus-fill" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M2 15.5V2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v13.5a.5.5 0 0 1-.74.439L8 13.069l-5.26 2.87A.5.5 0 0 1 2 15.5zm6.5-11a.5.5 0 0 0-1 0V6H6a.5.5 0 0 0 0 1h1.5v1.5a.5.5 0 0 0 1 0V7H10a.5.5 0 0 0 0-1H8.5V4.5z"/></svg></span>
					<span @click="addOrRemoveFromReadlist(book.slug)" v-if="!book.in_readlist" class="readlist-cursor position-absolute" style="top: 0rem; left: 0rem; z-index: 5;"><svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" fill="currentColor" class="bi bi-bookmark-plus" viewBox="0 0 16 16"><path d="M2 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v13.5a.5.5 0 0 1-.777.416L8 13.101l-5.223 2.815A.5.5 0 0 1 2 15.5V2zm2-1a1 1 0 0 0-1 1v12.566l4.723-2.482a.5.5 0 0 1 .554 0L13 14.566V2a1 1 0 0 0-1-1H4z"/><path d="M8 4a.5.5 0 0 1 .5.5V6H10a.5.5 0 0 1 0 1H8.5v1.5a.5.5 0 0 1-1 0V7H6a.5.5 0 0 1 0-1h1.5V4.5A.5.5 0 0 1 8 4z"/></svg></span>
					<router-link :to="`/book/${book.slug}`">
						<div class="profile-card-2"><img :src="`http://127.0.0.1:8000/media${book.thumbnail}`" class="img img-responsive">
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


			<!-- most popular authors -->
			<p class="h3 text-light warning-on-hover mb-2 mt-5">محبوب ترین نویسنده ها</p>
			<section class="container mt-5">
				<div class="row d-flex">

					<svg v-if="loading6" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" style="margin: auto; background: rgb(0, 0, 0); display: block;" width="184px" height="184px" viewBox="0 0 100 100" preserveAspectRatio="xMidYMid">
						<path d="M16 50A34 34 0 0 0 84 50A34 37.6 0 0 1 16 50" fill="#ffc200" stroke="none">
						<animateTransform attributeName="transform" type="rotate" dur="0.8695652173913042s" repeatCount="indefinite" keyTimes="0;1" values="0 50 51.8;360 50 51.8"></animateTransform>
						</path>
					</svg>
					
					<div v-for="a in popularAuthors" class="col-lg-3 col-md-3 col-sm-4 text-center mb-3">
						<router-link :to="`/author/${a.slug}`" class="text-decoration-none">
							<img class="rounded-circle mb-2 w-100 image-hover-reverse" :src="`http://127.0.0.1:8000/media${a.thumbnail}`" width="200px">
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
import { onMounted, ref } from "vue";
import { useStore } from 'vuex'
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'

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
				justGetData()
			})
			.catch(error => {
				if(error.response.status == 401){
					router.push('/login')
				}
			})

            document.getElementById('close-modal').click()

        }


        function justGetData(){

            axios
			.get('ShowBestBooks/')
			.then(response => {
				bestBooks.value = response.data.data
			})
			.catch(error => {
				console.log(error.response);
			})

			axios
			.get('ShowMostRatedBooks/')
			.then(response => {
				mostRatedBooks.value = response.data.data
			})
			.catch(error => {
				console.log(error.response);
			})
        }


		function addOrRemoveFromReadlist(sl){
			axios
			.post('AddOrRemoveFromReadlist/', {
				'slug': sl
			})
			.then(response => {
				justGetData()
			})
			.catch(error => {
				if(error.response.status == 401){
					router.push('/login')
				}
				console.log(error.response);
			})
		}
		


		return {
			modules: [Navigation, A11y],
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