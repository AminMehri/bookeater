<template>
    <div v-if="usernameExist" class="Activity">
        <div class="row g-0 position-relative">
            <img src="https://picsum.photos/800/200" alt="">
            <div class="col-3">
                <sidebar class="position-absolute" style="right: 15%; bottom: -10%;">
                    <img class="rounded-circle shadow-lg" src="https://picsum.photos/200" alt="">
                </sidebar>
            </div>
        </div>

        <div class="row mt-5 g-0">

            <div class="col-3">
                <p class="me-3">
                     کاربر: <h3>{{username}}</h3>
                </p>
            </div>

            <div class="col-8">
                <h5 class="mb-3">فعالیت ها</h5>
                <section class="Comment container ">
                    <p class="btn btn-outline-dark my-0">دیدگاه ها</p>
                    <div v-if="dataForShow" v-for="comment in comments" class="row border p-2 shadow text-end">
                        <p class="d-flex">
                            <p class="ms-3 text-end">{{comment.username}}</p>
                            <p>{{comment.date}}</p>
                        </p>
                        <p>{{comment.content}}</p>
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

                    <div v-if="!dataForShow">
                        <p class="alert alert-warning">چیزی جهت نمایش وجود ندارد.</p>
                    </div>
                </section>
            </div>

            <div class="col-1"></div>

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
import { ref, onMounted } from 'vue'
import { useStore } from 'vuex'
import { useRoute, useRouter } from 'vue-router';
import axios from 'axios'
import Swal from 'sweetalert2'


export default {
	setup() {
        const store = useStore()
        const route = useRoute();
        const router = useRouter();

        let username = ref(route.params.username)  

        let comments = ref('')

        let usernameExist = ref(true)

        let dataForShow = ref(true)
        
        function getData(){
            axios
            .post('ShowUserComment/', {
                slug: username.value
            })
            .then(response => {
                comments.value = response.data.data
                if(comments.value.length == 0){
                    dataForShow.value = false
                }
                usernameExist.value = true
            })
            .catch(error => {
                if(error.response.status == 404){
                    usernameExist.value = false
                }
                dataForShow.value = false
                console.log(error.response)
            })
        }
        getData()

		return {
            comments,
            username,
            usernameExist,
            dataForShow,
            getData,
		}
    
	},

}

</script>

<style scoped>
.not-found{
    font-size: clamp(7rem, 40vmin, 20rem);
}
</style>