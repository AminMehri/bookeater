<template>
    <div class="Readlist">
        <div class="container py-5">
            <div class="row text-center text-white mb-5">
                <div class="col-lg-7 mx-auto">
                    <h1 class="display-4 fw-bold text-dark">Product List</h1>
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
                                                <h5 class="card-title d-inline ms-5">{{book.title}}</h5>
                                                <a @click="takeSlug(book.slug)" href="#" class="fa fa-star" data-bs-toggle="modal" data-bs-target="#staticBackdrop"></a>
                                                <span class="fw-bold">{{book.user_score}}</span>
                                                <span class="fa fa-star checked me-3"></span>
                                                <span class="fw-bold">{{book.score}}</span>
                                                <span class="card-text d-block">{{book.description}}</span>
                                            </div>
                                        </div>
                                        <div class="col-md-4">
                                            <img :src="`http://127.0.0.1:8000/media${book.thumbnail}`" class="img-fluid rounded w-100" width="200px" alt="...">
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

export default {

    setup() {
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
            .get('ShowReadList/')
            .then(response => {
                books.value = response.data.data
                console.log(books.value);
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