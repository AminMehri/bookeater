<template>
    <div class="container text-center">
        <h1 class="mt-5">{{category.title}}</h1>
        <div class="row mt-4">
            <div class="col-md-8 mx-auto single-category p-md-4">
                <img @click="largerImage()" :src="`http://127.0.0.1:8000/media${category.image}`" class="img-fluid mb-4" id="larger_image">

                <p v-html="category.content"></p>


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

                <p class="h3 text-warning mb-0 mt-5">کتاب های مرتبط</p>
                <swiper
                    :modules="modules"
                    :breakpoints="swiperOptions.breakpoints"
                    navigation
                    >

                    <swiper-slide v-for="book in relatedBooks" class="position-relative">
                        <span @click="addOrRemoveFromReadlist(book.slug)" v-if="book.in_readlist" class="readlist-cursor position-absolute" style="top: 0rem; left: 0rem; z-index: 5;"><svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" fill="currentColor" class="bi bi-bookmark-plus-fill" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M2 15.5V2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v13.5a.5.5 0 0 1-.74.439L8 13.069l-5.26 2.87A.5.5 0 0 1 2 15.5zm6.5-11a.5.5 0 0 0-1 0V6H6a.5.5 0 0 0 0 1h1.5v1.5a.5.5 0 0 0 1 0V7H10a.5.5 0 0 0 0-1H8.5V4.5z"/></svg></span>
                        <span @click="addOrRemoveFromReadlist(book.slug)" v-if="!book.in_readlist" class="readlist-cursor position-absolute" style="top: 0rem; left: 0rem; z-index: 5;"><svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" fill="currentColor" class="bi bi-bookmark-plus" viewBox="0 0 16 16"><path d="M2 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v13.5a.5.5 0 0 1-.777.416L8 13.101l-5.223 2.815A.5.5 0 0 1 2 15.5V2zm2-1a1 1 0 0 0-1 1v12.566l4.723-2.482a.5.5 0 0 1 .554 0L13 14.566V2a1 1 0 0 0-1-1H4z"/><path d="M8 4a.5.5 0 0 1 .5.5V6H10a.5.5 0 0 1 0 1H8.5v1.5a.5.5 0 0 1-1 0V7H6a.5.5 0 0 1 0-1h1.5V4.5A.5.5 0 0 1 8 4z"/></svg></span>

                        <router-link :to="`/book/${book.slug}`">
                            <div class="profile-card-2"><img :src="`http://127.0.0.1:8000/media${book.thumbnail}`" class="img img-responsive">
                                <div class="book-name">{{book.title}}</div>
                                <div class="mx-auto book-star">
                                <span class="fw-bold ms-1 me-3">{{book.user_score}}</span>
                                <a @click="takeSlug(book.slug)" href="#" class="ms-4 fa fa-star" data-bs-toggle="modal" data-bs-target="#staticBackdrop"></a>
                                <span class="fa fa-star checked"></span>
                                <span class="fw-bold">{{book.score}}</span>
                                </div>
                            </div>
                        </router-link>
                    </swiper-slide>
                
                </swiper>

                <p class="h3 text-warning mb-2 mt-5">محبوب ترین نویسنده ها</p>

                <section class="container mt-5">
                    <div class="row d-flex">
                        
                            <div v-for="author in category.related_author" class="col-sm-4 col-6 text-center mb-3">
                                <router-link :to="`/author/${author[1]}`" class="text-decoration-none">
                                    <img class="rounded-circle mb-2 w-100" :src="`http://127.0.0.1:8000/media${author[2]}`" width="200px">
                                    <strong class="text-warning d-block h5">{{author[0]}}</strong>
                                </router-link>
                                
                                <p></p>
                            </div>

                    </div>

                </section>
            </div>
        </div>
    </div>
</template>


<script>
import { ref } from "vue";
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'

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
        const router = useRouter()

        let swiperOptions = {
			breakpoints: {       
				296: {       
					slidesPerView: 1,
				},          
				344: {       
					slidesPerView: 2,       
				},   

				500: {       
					slidesPerView: 3,       
				} 
			}
		}


        let slug = ref('')
        slug.value = route.params.slug

        let category = ref('')

        let relatedBooks = ref('')

        let slugForRate = ref('')

        let rate_number = ref('')

        function getData(){
            document.body.scrollTop = 0; // For Safari
            document.documentElement.scrollTop = 0;
            axios
            .post('ShowSingleCategory/', {
                slug: slug.value
            })
            .then(response => {
                category.value = response.data.category_data[0]
                relatedBooks.value = response.data.books_data
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
            .post('ShowSingleCategory/', {
                slug: slug.value
            })
            .then(response => {
                category.value = response.data.category_data[0]
                relatedBooks.value = response.data.books_data
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
            category,
            relatedBooks,
            swiperOptions,
            getData,
            takeSlug,
            sendRate,
            addOrRemoveFromReadlist,
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

@media screen and (max-width: 992px) {

    .book-name{
        font-size: 17px !important;
    }
    .book-star{
        font-size: 12px !important;
    }
}

@media screen and (max-width: 700px) {
    .book-star{
        font-size: 10px !important;
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

#larger_image:hover{
    cursor: all-scroll;
}
</style>