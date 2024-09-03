<template>

    <metainfo>
      <template v-slot:title="{ content }">{{ content }}</template>
    </metainfo>

    <div v-if="usernameExist" class="User">
        <div class="row g-0 position-relative">
            <img v-if="images[0].image != 'null'" :src="`https://api.bookeater.ir/media${images[0].image}`" class="w-100" height="400">
            <div class="col-3">
                <sidebar class="position-absolute" style="right: 15%; bottom: -10%;">
                    <img v-if="images[0].thumbnail != 'null'" :src="`https://api.bookeater.ir/media${images[0].thumbnail}`" class="rounded-circle shadow-lg img-thumbnail" height="200" width="200" :alt="`${images[0].full_name}`" :title="`${images[0].full_name}`">
                </sidebar>
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

        <div class="row mt-5 g-0">

            <div class="col-lg-2 col-md-3 col-sm-4">
                <p class="me-3">
                     کاربر: <p class="h3">{{username}}</p>
                </p>
            </div>

            <div class="col-lg-9 col-md-8 col-sm-7 container-fluid g-0">
                <h5 class="mb-3">فعالیت ها</h5>

                <p v-if="!showComment" @click="showCommentFunc()" class="btn btn-outline-dark my-0 w-50">دیدگاه ها</p>
                <p v-if="showComment" @click="showCommentFunc()" class="btn btn-dark my-0 w-50">دیدگاه ها</p>
                <p v-if="!showVoteBook" @click="showVoteBookFunc()" class="btn btn-outline-dark my-0 w-50">رای ها</p>
                <p v-if="showVoteBook" @click="showVoteBookFunc()" class="btn btn-dark my-0 w-50">رای ها</p>

                <section v-if="showComment" class="Comment container mt-5">
                    <p>مرتب کردن بر اساس:</p>
                    <svg v-if=upToDown @click="upToDown = !upToDown" xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-arrow-down" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M8 1a.5.5 0 0 1 .5.5v11.793l3.146-3.147a.5.5 0 0 1 .708.708l-4 4a.5.5 0 0 1-.708 0l-4-4a.5.5 0 0 1 .708-.708L7.5 13.293V1.5A.5.5 0 0 1 8 1z"/></svg>
                    <svg v-if=!upToDown @click="upToDown = !upToDown" xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-arrow-up" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M8 15a.5.5 0 0 0 .5-.5V2.707l3.146 3.147a.5.5 0 0 0 .708-.708l-4-4a.5.5 0 0 0-.708 0l-4 4a.5.5 0 1 0 .708.708L7.5 2.707V14.5a.5.5 0 0 0 .5.5z"/></svg>
                    <span @click="filterLike()" class="btn btn-primary mb-2 mx-3">لایک</span>
                    <span @click="filterDisLike()" class="btn btn-primary mb-2 ">دیس لایک</span>
                    <span @click="filterDate()" class="btn btn-primary mb-2 mx-3">تاریخ</span>
                    <div v-if="commentDataForShow" v-for="comment in comments" class="row border p-2 shadow text-end">
                        <p class="d-flex">
                            <p class="ms-3 text-end">{{comment.username}}</p>
                            <p>{{comment.date}}</p>
                        </p>
                        <p v-html="comment.content"></p>
                        <p>
                            <span class="ms-1">{{comment.like}}</span>
                            <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" viewBox="0 0 512 512"><!--! Font Awesome Pro 6.1.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. --><path d="M96 191.1H32c-17.67 0-32 14.33-32 31.1v223.1c0 17.67 14.33 31.1 32 31.1h64c17.67 0 32-14.33 32-31.1V223.1C128 206.3 113.7 191.1 96 191.1zM512 227c0-36.89-30.05-66.92-66.97-66.92h-99.86C354.7 135.1 360 113.5 360 100.8c0-33.8-26.2-68.78-70.06-68.78c-46.61 0-59.36 32.44-69.61 58.5c-31.66 80.5-60.33 66.39-60.33 93.47c0 12.84 10.36 23.99 24.02 23.99c5.256 0 10.55-1.721 14.97-5.26c76.76-61.37 57.97-122.7 90.95-122.7c16.08 0 22.06 12.75 22.06 20.79c0 7.404-7.594 39.55-25.55 71.59c-2.046 3.646-3.066 7.686-3.066 11.72c0 13.92 11.43 23.1 24 23.1h137.6C455.5 208.1 464 216.6 464 227c0 9.809-7.766 18.03-17.67 18.71c-12.66 .8593-22.36 11.4-22.36 23.94c0 15.47 11.39 15.95 11.39 28.91c0 25.37-35.03 12.34-35.03 42.15c0 11.22 6.392 13.03 6.392 22.25c0 22.66-29.77 13.76-29.77 40.64c0 4.515 1.11 5.961 1.11 9.456c0 10.45-8.516 18.95-18.97 18.95h-52.53c-25.62 0-51.02-8.466-71.5-23.81l-36.66-27.51c-4.315-3.245-9.37-4.811-14.38-4.811c-13.85 0-24.03 11.38-24.03 24.04c0 7.287 3.312 14.42 9.596 19.13l36.67 27.52C235 468.1 270.6 480 306.6 480h52.53c35.33 0 64.36-27.49 66.8-62.2c17.77-12.23 28.83-32.51 28.83-54.83c0-3.046-.2187-6.107-.6406-9.122c17.84-12.15 29.28-32.58 29.28-55.28c0-5.311-.6406-10.54-1.875-15.64C499.9 270.1 512 250.2 512 227z"/></svg>
                            <span class="me-4 ms-1">{{comment.dis_like}}</span>
                            <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" viewBox="0 0 512 512"><!--! Font Awesome Pro 6.1.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. --><path d="M128 288V64.03c0-17.67-14.33-31.1-32-31.1H32c-17.67 0-32 14.33-32 31.1v223.1c0 17.67 14.33 31.1 32 31.1h64C113.7 320 128 305.7 128 288zM481.5 229.1c1.234-5.092 1.875-10.32 1.875-15.64c0-22.7-11.44-43.13-29.28-55.28c.4219-3.015 .6406-6.076 .6406-9.122c0-22.32-11.06-42.6-28.83-54.83c-2.438-34.71-31.47-62.2-66.8-62.2h-52.53c-35.94 0-71.55 11.87-100.3 33.41L169.6 92.93c-6.285 4.71-9.596 11.85-9.596 19.13c0 12.76 10.29 24.04 24.03 24.04c5.013 0 10.07-1.565 14.38-4.811l36.66-27.51c20.48-15.34 45.88-23.81 71.5-23.81h52.53c10.45 0 18.97 8.497 18.97 18.95c0 3.5-1.11 4.94-1.11 9.456c0 26.97 29.77 17.91 29.77 40.64c0 9.254-6.392 10.96-6.392 22.25c0 13.97 10.85 21.95 19.58 23.59c8.953 1.671 15.45 9.481 15.45 18.56c0 13.04-11.39 13.37-11.39 28.91c0 12.54 9.702 23.08 22.36 23.94C456.2 266.1 464 275.2 464 284.1c0 10.43-8.516 18.93-18.97 18.93H307.4c-12.44 0-24 10.02-24 23.1c0 4.038 1.02 8.078 3.066 11.72C304.4 371.7 312 403.8 312 411.2c0 8.044-5.984 20.79-22.06 20.79c-12.53 0-14.27-.9059-24.94-28.07c-24.75-62.91-61.74-99.9-80.98-99.9c-13.8 0-24.02 11.27-24.02 23.99c0 7.041 3.083 14.02 9.016 18.76C238.1 402 211.4 480 289.9 480C333.8 480 360 445 360 411.2c0-12.7-5.328-35.21-14.83-59.33h99.86C481.1 351.9 512 321.9 512 284.1C512 261.8 499.9 241 481.5 229.1z"/></svg>
                        </p>
                        <p>
                            دیدگاه در کتاب: <router-link class="text-danger" :to="`/book/${comment.book_slug}`">{{comment.book_title}}</router-link>
                        </p>

                    </div>

                    <div v-if="!commentDataForShow">
                        <p class="alert alert-warning">دیدگاهی جهت نمایش وجود ندارد.</p>
                    </div>
                </section>

                <section v-if="showVoteBook" class="Vote container mt-5">
                    <div v-if="bookDataForShow" class="row">
                        <div class=" mb-4">
                            <div class="text-center">
                                <p>مرتب کردن بر اساس:</p>
                                <svg v-if=upToDown @click="upToDown = !upToDown" xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-arrow-down" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M8 1a.5.5 0 0 1 .5.5v11.793l3.146-3.147a.5.5 0 0 1 .708.708l-4 4a.5.5 0 0 1-.708 0l-4-4a.5.5 0 0 1 .708-.708L7.5 13.293V1.5A.5.5 0 0 1 8 1z"/></svg>
                                <svg v-if=!upToDown @click="upToDown = !upToDown" xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-arrow-up" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M8 15a.5.5 0 0 0 .5-.5V2.707l3.146 3.147a.5.5 0 0 0 .708-.708l-4-4a.5.5 0 0 0-.708 0l-4 4a.5.5 0 1 0 .708.708L7.5 2.707V14.5a.5.5 0 0 0 .5.5z"/></svg>
                                <span @click="filterScore()" class="btn btn-primary mb-2 mx-3">نمره</span>
                                <span @click="filterRate()" class="btn btn-primary mb-2 ">رای</span>
                                <span @click="filterUserRate()" class="btn btn-primary mb-2 mx-3">نمره کاربر</span>
                            </div>
                        </div>
                        <div class="col-lg-9 mx-auto">

                            <ul v-for="book in books" class="list-group position-relative">
                                <span @click="addOrRemoveFromReadlist(book.slug)" v-if="book.in_readlist" class="readlist-cursor text-dark position-absolute" style="top: 0rem; left: 0rem; z-index: 5;"><svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" fill="currentColor" class="bi bi-bookmark-plus-fill" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M2 15.5V2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v13.5a.5.5 0 0 1-.74.439L8 13.069l-5.26 2.87A.5.5 0 0 1 2 15.5zm6.5-11a.5.5 0 0 0-1 0V6H6a.5.5 0 0 0 0 1h1.5v1.5a.5.5 0 0 0 1 0V7H10a.5.5 0 0 0 0-1H8.5V4.5z"/></svg></span>
                                <span @click="addOrRemoveFromReadlist(book.slug)" v-if="!book.in_readlist" class="readlist-cursor text-dark position-absolute" style="top: 0rem; left: 0rem; z-index: 5;"><svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" fill="currentColor" class="bi bi-bookmark-plus" viewBox="0 0 16 16"><path d="M2 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v13.5a.5.5 0 0 1-.777.416L8 13.101l-5.223 2.815A.5.5 0 0 1 2 15.5V2zm2-1a1 1 0 0 0-1 1v12.566l4.723-2.482a.5.5 0 0 1 .554 0L13 14.566V2a1 1 0 0 0-1-1H4z"/><path d="M8 4a.5.5 0 0 1 .5.5V6H10a.5.5 0 0 1 0 1H8.5v1.5a.5.5 0 0 1-1 0V7H6a.5.5 0 0 1 0-1h1.5V4.5A.5.5 0 0 1 8 4z"/></svg></span>

                                <router-link :to="`/book/${book.slug}`">

                                    <li class="list-group-item">

                                        <div class=" mb-3">
                                            <div class="row g-0">
                                                <div class="col-md-8">
                                                    <div class="card-body">
                                                        <div class="d-block">
                                                            <span class="fa fa-star text-danger"></span>
                                                            <span class="fw-bold">{{book.target_user_score}}</span>
                                                        </div>
                                                        <h5 class="card-title d-inline ms-5">{{book.title}}</h5>
                                                        <a @click="takeSlug(book.slug)" href="#" class="fa fa-star" data-bs-toggle="modal" data-bs-target="#staticBackdrop"></a>
                                                        <span class="fw-bold">{{book.user_score}}</span>
                                                        <span class="text-muted me-3">({{book.rates}})</span>
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

                    <div v-if="!bookDataForShow">
                        <p class="alert alert-warning">کتابی جهت نمایش وجود ندارد.</p>
                    </div>

                </section>
            </div>

        </div>
    </div>
    <div v-if="!usernameExist">
        <div class="PageNotFound bg-dark">
            <div class="container text-center p-5">
                <h1 class="not-found text-muted">404</h1>
                <p class="text-light">صفحه مورد نظر شما یافت نشد.</p>
                <hr class="text-white">    
            </div>

        </div>
    </div>
</template>

<script>
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router';
import axios from 'axios'
import { useMeta } from 'vue-meta'


export default {
	setup() {
        const route = useRoute();
        
        useMeta({
            robots: "index, follow",
            keywords: "کتاب خوار, کتاب, نویسنده, نقد کتاب, کتابخانه, دسته بندی های کتاب, برترین کتاب ها",
            googlebot: "index, follow",
            author: "امین مهری",
            owner: "امین مهری",
            canonical: `https://bookeater.ir/user/${route.params.username}`,
            'og:type': `${route.params.username}-bookeater`,
            'og:title': "bookeater",
            'og:site_name': "کتاب خوار",
            'og:url': `https://bookeater.ir/user/${route.params.username}`,
            'og:image': "https://bookeater.ir/media/image.jpg",
            'twitter:title': "کتاب خوار",
            'twitter:description': "کتاب هایی با بیشترین نمره را در سایت کتاب خوار گرفته اند. شما نیز میتوانید یکی از رای دهندگان به این کتاب باشید.",
            'twitter:site': "https://twitter.com/aminem_mehri",
            'twitter:card': "Summary Card",
            'twitter:image': "https://bookeater.ir/media/image.jpg",
        });

        const router = useRouter();

        let username = ref(route.params.username)  

        let comments = ref('')

        let usernameExist = ref(true)

        let commentDataForShow = ref(true)

        let bookDataForShow = ref(true)

        let images = ref()

        let books = ref()

        let showComment = ref(true)
        let showVoteBook = ref(false)


        let slugForRate = ref('')
        let rate_number = ref('')


        function showCommentFunc(){
            showComment.value = true
            showVoteBook.value = false
        }

        function showVoteBookFunc(){
            showComment.value = false
            showVoteBook.value = true
        }

        
        function getData(){
            axios
            .post('ShowUserComment/', {
                slug: username.value
            })
            .then(response => {
                comments.value = response.data.data
                images.value = response.data.user_images_data
                if(comments.value.length == 0){
                    commentDataForShow.value = false
                }
                usernameExist.value = true
                document.title = "کتابخوار | " + comments.value[0].username
            })
            .catch(error => {
                if(error.response.status == 404){
                    usernameExist.value = false
                }
                commentDataForShow.value = false
                console.log(error.response)
            })


            axios
            .post('ShowUserVotes/', {
                slug: username.value
            })
            .then(response => {
                books.value = response.data.data

                books.value.length == 0 ? bookDataForShow.value = false : bookDataForShow.value = true;
            })
            .catch(error => {
                if(error.response.status == 404){
                    bookDataForShow.value = false
                }
                console.log(error.response)
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
                    return b.target_user_score - a.target_user_score;
                })
            } else {
                books.value.sort(function(a , b) {
                    return a.target_user_score - b.target_user_score;
                })
            }
        }

        // comment filter
        function filterLike(){
            upToDown.value = !upToDown.value
            if(upToDown.value){
                comments.value.sort(function(a , b) {
                    return b.like - a.like;
                })
            } else {
                comments.value.sort(function(a , b) {
                    return a.like - b.like;
                })
            }
        }

        function filterDisLike(){
            upToDown.value = !upToDown.value
            if(upToDown.value){
                comments.value.sort(function(a , b) {
                    return b.dis_like - a.dis_like;
                })
            } else {
                comments.value.sort(function(a , b) {
                    return a.dis_like - b.dis_like;
                })
            }
        }

        function filterDate(){
            upToDown.value = !upToDown.value
            if(upToDown.value){
                comments.value.sort(function(a , b) {
                    return b.date_for_filter - a.date_for_filter;
                })
            } else {
                comments.value.sort(function(a , b) {
                    return a.date_for_filter - b.date_for_filter;
                })
            }
        }

		return {
            comments,
            username,
            usernameExist,
            commentDataForShow,
            images,
            showComment,
            showVoteBook,
            books,
            bookDataForShow,
            slugForRate,
            rate_number,
            upToDown,
            getData,
            showCommentFunc,
            showVoteBookFunc,
            addOrRemoveFromReadlist,
            takeSlug,
            sendRate,
            filterScore,
            filterRate,
            filterUserRate,
            filterLike,
            filterDisLike,
            filterDate,
		}
    
	},

}

</script>

<style scoped>
.not-found{
    font-size: clamp(7rem, 40vmin, 20rem);
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