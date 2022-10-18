<template>

    <metainfo>
      <template v-slot:title="{ content }">{{ content }}</template>
    </metainfo>

    <div class="Readlist">
        <div class="container py-5">
            <div class="row text-center text-white mb-5">
                <div class="col-lg-7 mx-auto">
                    <h1 class="display-4 fw-bold text-dark">خواندنی ها</h1>
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

            <div class="row mb-4">
                <div class="text-center">
                    <p>مرتب کردن بر اساس:</p>
                    <svg v-if=upToDown @click="upToDown = !upToDown" xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-arrow-down" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M8 1a.5.5 0 0 1 .5.5v11.793l3.146-3.147a.5.5 0 0 1 .708.708l-4 4a.5.5 0 0 1-.708 0l-4-4a.5.5 0 0 1 .708-.708L7.5 13.293V1.5A.5.5 0 0 1 8 1z"/></svg>
                    <svg v-if=!upToDown @click="upToDown = !upToDown" xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-arrow-up" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M8 15a.5.5 0 0 0 .5-.5V2.707l3.146 3.147a.5.5 0 0 0 .708-.708l-4-4a.5.5 0 0 0-.708 0l-4 4a.5.5 0 1 0 .708.708L7.5 2.707V14.5a.5.5 0 0 0 .5.5z"/></svg>
                    <span @click="filterScore()" class="btn btn-primary mb-2 mx-3">نمره</span>
                    <span @click="filterRate()" class="btn btn-primary mb-2 ">رای</span>
                    <span @click="filterUserRate()" class="btn btn-primary mb-2 mx-3">نمره کاربر</span>
                </div>
            </div>


            <div class="row">
                <div class="col-lg-9 mx-auto">

                    <ul v-for="book in books" class="list-group shadow position-relative">
                        <span @click="addOrRemoveFromReadlist(book.slug)" v-if="book.in_readlist" class="readlist-cursor text-dark position-absolute" style="top: 0rem; left: 0rem; z-index: 5;"><svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" fill="currentColor" class="bi bi-bookmark-plus-fill" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M2 15.5V2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v13.5a.5.5 0 0 1-.74.439L8 13.069l-5.26 2.87A.5.5 0 0 1 2 15.5zm6.5-11a.5.5 0 0 0-1 0V6H6a.5.5 0 0 0 0 1h1.5v1.5a.5.5 0 0 0 1 0V7H10a.5.5 0 0 0 0-1H8.5V4.5z"/></svg></span>
                        <span @click="addOrRemoveFromReadlist(book.slug)" v-if="!book.in_readlist" class="readlist-cursor text-dark position-absolute" style="top: 0rem; left: 0rem; z-index: 5;"><svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" fill="currentColor" class="bi bi-bookmark-plus" viewBox="0 0 16 16"><path d="M2 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v13.5a.5.5 0 0 1-.777.416L8 13.101l-5.223 2.815A.5.5 0 0 1 2 15.5V2zm2-1a1 1 0 0 0-1 1v12.566l4.723-2.482a.5.5 0 0 1 .554 0L13 14.566V2a1 1 0 0 0-1-1H4z"/><path d="M8 4a.5.5 0 0 1 .5.5V6H10a.5.5 0 0 1 0 1H8.5v1.5a.5.5 0 0 1-1 0V7H6a.5.5 0 0 1 0-1h1.5V4.5A.5.5 0 0 1 8 4z"/></svg></span>

                        <router-link :to="`/book/${book.slug}`" class="">

                            <li class="list-group-item">

                                <div class=" mb-3">
                                    <div class="row g-0">
                                        <div class="col-md-8">
                                            <div class="card-body">
                                                <h5 class="card-title d-inline ms-sm-5 ms-1 d-block d-sm-inline">{{book.title}}</h5>
                                                <a @click="takeSlug(book.slug)" href="#" class="fa fa-star" data-bs-toggle="modal" data-bs-target="#staticBackdrop"></a>
                                                <span class="fw-bold" id="user_score">{{book.user_score}}</span>
                                                <span class="me-3 text-muted">({{book.rates}})</span>
                                                <span class="fa fa-star checked"></span>
                                                <span class="fw-bold">{{book.score}}</span>
                                                <span v-html="book.description" class="card-text d-block"></span>
                                            </div>
                                        </div>
                                        <div class="col-md-4">
                                            <img :src="`https://api.bookeater.ir/media${book.thumbnail}`" class="img-fluid rounded w-100" width="200px" :alt="`${book.title}`" :title="`${book.title}`">
                                        </div>
                                    </div>
                                </div>
                            </li> 
                        </router-link>

                    </ul>
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
import { useMeta } from 'vue-meta'

export default {
    setup() {
        useMeta({
            title: "کتاب های خواندنی من | کتاب خوار",
            robots: "noindex, nofollow",
            googlebot: "noindex, nofollow",
        });

        const store = useStore()
        const route = useRoute()
        const router = useRouter()

        let books = ref('')

        let slugForRate = ref('')
        let rate_number = ref('')

        function getData(){
            document.body.scrollTop = 0; // For Safari
            document.documentElement.scrollTop = 0;
            axios
            .get('ShowReadList/')
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

        // book filter
        let upToDown = ref(true)
        function filterScore(){
            upToDown.value = !upToDown.value
            if(upToDown.value){
                books.value.sort(function(a , b) {
                    return b.score - a.score;
                })
            } else {
                books.value.sort(function(a , b) {
                    return a.score - b.score;
                })
            }
        }

        function filterRate(){
            upToDown.value = !upToDown.value
            if(upToDown.value){
                books.value.sort(function(a , b) {
                    return b.rates - a.rates;
                })
            } else {
                books.value.sort(function(a , b) {
                    return a.rates - b.rates;
                })
            }
        }

        function filterUserRate(){
            upToDown.value = !upToDown.value
            if(upToDown.value){
                books.value.sort(function(a , b) {
                    return b.user_score - a.user_score;
                })
            } else {
                books.value.sort(function(a , b) {
                    return a.user_score - b.user_score;
                })
            }
        }

        return {
            books,
            upToDown,
            getData,
            takeSlug,
            sendRate,
            addOrRemoveFromReadlist,
            filterScore,
            filterRate,
            filterUserRate,
        };
    },
};
</script>


<style scoped>
.Readlist{
    background: rgb(255,255,255);
    background: linear-gradient(90deg, rgba(255,255,255,1) 0%, rgba(236,145,182,1) 100%);
    min-height: 100vh;
}

.list-group-item{
    border: none;
}
.list-group-item:hover{
    border: 3px;
    box-shadow: rgba(0, 0, 0, 0.24) 5px 5px 15px 10px;
    transition-duration: 0.25s;
}
.text-gray{
    color: #aaa
}

.checked{
    color: orange;
}

</style>