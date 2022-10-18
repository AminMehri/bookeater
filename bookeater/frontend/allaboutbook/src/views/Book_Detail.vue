<template>

    <metainfo>
      <template v-slot:title="{ content }">{{ content }}</template>
    </metainfo>

    <div v-if="!return404" id="Single-Book">
        <div v-for="b in book" class="container text-center">
            <h1 id="title_book" class="mt-5">{{b.title}}</h1>
            <span class="fw-bold ms-1 fs-3" id="book-score">{{b.user_score}}</span>
            <a href="#" class="ms-4 fa fa-star fs-3" data-bs-toggle="modal" data-bs-target="#staticBackdrop"></a>
            <span class="text-muted">({{b.rates}})</span>
            <span class="fa fa-star checked fs-3"></span>
            <span class="fw-bold fs-3">{{b.score}}</span>
            <span @click="addOrRemoveFromReadlist(b.slug)" v-if="b.in_readlist" class="readlist-cursor"><svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" fill="currentColor" class="bi bi-bookmark-plus-fill" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M2 15.5V2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v13.5a.5.5 0 0 1-.74.439L8 13.069l-5.26 2.87A.5.5 0 0 1 2 15.5zm6.5-11a.5.5 0 0 0-1 0V6H6a.5.5 0 0 0 0 1h1.5v1.5a.5.5 0 0 0 1 0V7H10a.5.5 0 0 0 0-1H8.5V4.5z"/></svg></span>
			<span @click="addOrRemoveFromReadlist(b.slug)" v-if="!b.in_readlist" class="readlist-cursor"><svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" fill="currentColor" class="bi bi-bookmark-plus" viewBox="0 0 16 16"><path d="M2 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v13.5a.5.5 0 0 1-.777.416L8 13.101l-5.223 2.815A.5.5 0 0 1 2 15.5V2zm2-1a1 1 0 0 0-1 1v12.566l4.723-2.482a.5.5 0 0 1 .554 0L13 14.566V2a1 1 0 0 0-1-1H4z"/><path d="M8 4a.5.5 0 0 1 .5.5V6H10a.5.5 0 0 1 0 1H8.5v1.5a.5.5 0 0 1-1 0V7H6a.5.5 0 0 1 0-1h1.5V4.5A.5.5 0 0 1 8 4z"/></svg></span>
            <router-link v-for="a in b.author" :to="`/author/${a[1]}`" class="text-muted h2 d-block author-link">{{a[0]}}</router-link>


            <div class="row mt-4">
                <div class="col-md-8 mx-auto single-category p-sm-4">
                    <img @click="largerImage()" :src="`https://api.bookeater.ir/media${b.image}`" class="img-fluid mb-4" id="larger_image" :alt="`${b.title}`" :title="`${b.title}`">

                    <p id="content_book" v-html="b.content"></p>


                    <!-- Modal star rating detail book-->
                    <div class="modal fade" id="staticBackdrop" tabindex="-1">
                        <div class="modal-dialog modal-dialog-centered">
                            <div class="modal-content bg-dark p-sm-3 p-0">
                                <div class="modal-body mx-auto text-center">
                                    <div class="mx-auto star-rating text-white fs-4">
                                        <span @click="sendRate(1, slug)" class="fa fa-star"></span>
                                        <span @click="sendRate(2, slug)" class="fa fa-star"></span>
                                        <span @click="sendRate(3, slug)" class="fa fa-star"></span>
                                        <span @click="sendRate(4, slug)" class="fa fa-star"></span>
                                        <span @click="sendRate(5, slug)" class="fa fa-star"></span>
                                        <span @click="sendRate(6, slug)" class="fa fa-star"></span>
                                        <span @click="sendRate(7, slug)" class="fa fa-star"></span>
                                        <span @click="sendRate(8, slug)" class="fa fa-star"></span>
                                        <span @click="sendRate(9, slug)" class="fa fa-star"></span>
                                        <span @click="sendRate(10, slug)" class="fa fa-star"></span>
                                    </div>
                                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal" id="close-modal" hidden>Close</button>
                                </div>
                            </div>
                        </div>
                    </div>


                    <!-- Modal star rating related book -->
                    <div class="modal fade w-100" id="staticBackdrop2" tabindex="-1">
                        <div class="modal-dialog modal-dialog-centered">
                            <div class="modal-content bg-dark p-sm-3 p-0">
                                <div class="modal-body mx-auto text-center">
                                    <div class="mx-auto star-rating text-white fs-4">
                                        <span @click="sendRate(1, book.slug)" class="fa fa-star"></span>
                                        <span @click="sendRate(2, book.slug)" class="fa fa-star"></span>
                                        <span @click="sendRate(3, book.slug)" class="fa fa-star"></span>
                                        <span @click="sendRate(4, book.slug)" class="fa fa-star"></span>
                                        <span @click="sendRate(5, book.slug)" class="fa fa-star"></span>
                                        <span @click="sendRate(6, book.slug)" class="fa fa-star"></span>
                                        <span @click="sendRate(7, book.slug)" class="fa fa-star"></span>
                                        <span @click="sendRate(8, book.slug)" class="fa fa-star"></span>
                                        <span @click="sendRate(9, book.slug)" class="fa fa-star"></span>
                                        <span @click="sendRate(10, book.slug)" class="fa fa-star"></span>
                                    </div>
                                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal" id="close-modal2" hidden>Close</button>
                                </div>
                            </div>
                        </div>
                    </div>


                    <!-- Modal report-->
                    <div class="modal" id="staticBackdrop3" tabindex="-1">
                        <div class="modal-dialog modal-dialog-centered">
                            <div class="modal-content p-sm-3 p-0">
                                <div class="modal-body mx-auto text-center">
                                    <div class="mx-auto star-rating text-dark">
                                        <h3>گزارش تخلف</h3>
                                        <label for="inputDescription" class="form-label mt-3">توضیحات</label>
                                        <textarea v-model="cause" class="form-control" id="inputDescription" cols="30" rows="6"></textarea>
                                        <button @click="report()" class="btn btn-primary mt-2">ارسال</button>
                                    </div>
                                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal" id="close-modal3" hidden>Close</button>
                                </div>
                            </div>
                        </div>
                    </div>


                    <!-- Modal reply comment-->
                    <div class="modal" id="staticBackdrop4" tabindex="-1">
                        <div class="modal-dialog modal-dialog-centered">
                            <div class="modal-content p-sm-3 p-0">
                                <div class="modal-body mx-auto text-center">
                                    <div class="mx-auto star-rating text-dark">
                                        <h3>پاسخ به</h3>
                                        <label for="inputDescription" class="form-label mt-3">توضیحات</label>
                                        <textarea v-model="commentContent" class="form-control" id="inputDescription" cols="30" rows="6"></textarea>
                                        <button @click="makeComment()" class="btn btn-primary mt-2">ارسال</button>
                                    </div>
                                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal" id="close-modal4" hidden>Close</button>
                                </div>
                            </div>
                        </div>
                    </div>
                    


                    <p class="h3 text-warning mb-0 mt-5">کتاب های مرتبط</p>
                    <swiper
                        :modules="modules"
                        :breakpoints="swiperOptions.breakpoints"
                        :loop="true"
                        navigation
                        >

                        <swiper-slide v-for="book in relatedBooks" class="position-relative" height="500px">
                            <span @click="addOrRemoveFromReadlist(book.slug)" v-if="book.in_readlist" class="readlist-cursor position-absolute" style="top: 0rem; left: 0rem; z-index: 5;"><svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" fill="currentColor" class="bi bi-bookmark-plus-fill" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M2 15.5V2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v13.5a.5.5 0 0 1-.74.439L8 13.069l-5.26 2.87A.5.5 0 0 1 2 15.5zm6.5-11a.5.5 0 0 0-1 0V6H6a.5.5 0 0 0 0 1h1.5v1.5a.5.5 0 0 0 1 0V7H10a.5.5 0 0 0 0-1H8.5V4.5z"/></svg></span>
					        <span @click="addOrRemoveFromReadlist(book.slug)" v-if="!book.in_readlist" class="readlist-cursor position-absolute" style="top: 0rem; left: 0rem; z-index: 5;"><svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" fill="currentColor" class="bi bi-bookmark-plus" viewBox="0 0 16 16"><path d="M2 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v13.5a.5.5 0 0 1-.777.416L8 13.101l-5.223 2.815A.5.5 0 0 1 2 15.5V2zm2-1a1 1 0 0 0-1 1v12.566l4.723-2.482a.5.5 0 0 1 .554 0L13 14.566V2a1 1 0 0 0-1-1H4z"/><path d="M8 4a.5.5 0 0 1 .5.5V6H10a.5.5 0 0 1 0 1H8.5v1.5a.5.5 0 0 1-1 0V7H6a.5.5 0 0 1 0-1h1.5V4.5A.5.5 0 0 1 8 4z"/></svg></span>

                            <router-link @click="getData(book.slug); getComments()" :to="`/book/${book.slug}`">
                                <div class="profile-card-2" height="500px"><img :src="`https://api.bookeater.ir/media${book.thumbnail}`" class="img img-responsive" :alt="`${book.title}`" :title="`${book.title}`">
                                    <div class="book-name">{{book.title}}</div>
                                </div>
                            </router-link>
                            <div class="mx-auto book-star">
                                <span class="fw-bold ms-1">{{book.user_score}}</span>
                                <a @click="takeSlug(book.slug)" href="#" class="ms-4 fa fa-star" data-bs-toggle="modal" data-bs-target="#staticBackdrop2"></a>
                                <span class="fa fa-star checked"></span>
                                <span class="fw-bold">{{book.score}}</span>
                            </div>
                        </swiper-slide>
                    
                    </swiper>

                    <p class="h3 text-warning mb-2 mt-5">کتاب های دیگر نویسنده</p>

                    <section class="container mt-5">
                        <div class="row d-flex">
                            
                                <div v-for="book in author_books" class="col-lg-3 col-md-3 col-sm-4 col-6 text-center mb-3">
                                    <router-link @click="getData(book.slug); getComments()" :to="`/book/${book.slug}`" class="text-decoration-none">
                                        <img class="rounded-circle mb-2 w-100" :src="`https://api.bookeater.ir/media${book.thumbnail}`" width="200px" :alt="`${book.title}`" :title="`${book.title}`">
                                        <strong class="text-warning d-block h5">{{book.title}}</strong>
                                    </router-link>
                                    
                                    <p></p>
                                </div>

                        </div>

                    </section>

                    <div v-if="$store.state.isAuthenticated" class="Make-Comment">
                        <h3 class="text-center">گذاشتن کامنت</h3>
                        <div class="row g-3 border p-4">
                            
                            <div class="col-12">
                                <label for="inputContent" class="form-label">محتوا</label>
                                <textarea v-model="commentContent" class="form-control" id="inputContent" rows="10"></textarea>
                            </div>

                            <div class="col-12">
                                <button @click="makeComment()" class="btn btn-primary">ثبت دیدگاه</button>
                            </div>
                        </div>
                    </div>

                    <div v-if="!$store.state.isAuthenticated" class="alert alert-warning">برای ثبت دیدگاه لطفا <router-link to="/login">لاگین</router-link> کنید</div>

                    <section class="Comment container ">
                        <h4>دیدگاه ها</h4>

                        <p>مرتب کردن بر اساس:</p>
                        <svg v-if=upToDown @click="upToDown = !upToDown" xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-arrow-down" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M8 1a.5.5 0 0 1 .5.5v11.793l3.146-3.147a.5.5 0 0 1 .708.708l-4 4a.5.5 0 0 1-.708 0l-4-4a.5.5 0 0 1 .708-.708L7.5 13.293V1.5A.5.5 0 0 1 8 1z"/></svg>
                        <svg v-if=!upToDown @click="upToDown = !upToDown" xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-arrow-up" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M8 15a.5.5 0 0 0 .5-.5V2.707l3.146 3.147a.5.5 0 0 0 .708-.708l-4-4a.5.5 0 0 0-.708 0l-4 4a.5.5 0 1 0 .708.708L7.5 2.707V14.5a.5.5 0 0 0 .5.5z"/></svg>
                        <span @click="filterLike()" class="btn btn-primary mb-2 mx-3">لایک</span>
                        <span @click="filterDisLike()" class="btn btn-primary mb-2 ">دیس لایک</span>
                        <span @click="filterHottest()" class="btn btn-primary mb-2 mx-3">داغ ترین ها</span>
                        <span @click="filterDate()" class="btn btn-primary mb-2 mx-3">تاریخ</span>

                        <div v-for="comment in comments" class="row border text-end">
                            <div v-if="comment.reply_to == 'null'">
                                <p class="d-flex">
                                    <p class="ms-3 text-end"><router-link :to="`/user/${comment.username_slug}`">{{comment.username}}</router-link></p>
                                    <p>{{comment.date}}</p>
                                    <p @click="takeIdReply(comment.id)" title="ریپلای" class="me-auto custom-cursor" data-bs-toggle="modal" data-bs-target="#staticBackdrop4"><svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-reply-fill" viewBox="0 0 16 16"><path d="M5.921 11.9 1.353 8.62a.719.719 0 0 1 0-1.238L5.921 4.1A.716.716 0 0 1 7 4.719V6c1.5 0 6 0 7 8-2.5-4.5-7-4-7-4v1.281c0 .56-.606.898-1.079.62z"/></svg></p>
                                    <p @click="takeId(comment.id)" title="گزارش تخلف" class="me-2 custom-cursor" data-bs-toggle="modal" data-bs-target="#staticBackdrop3"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-flag-fill" viewBox="0 0 16 16"><path d="M14.778.085A.5.5 0 0 1 15 .5V8a.5.5 0 0 1-.314.464L14.5 8l.186.464-.003.001-.006.003-.023.009a12.435 12.435 0 0 1-.397.15c-.264.095-.631.223-1.047.35-.816.252-1.879.523-2.71.523-.847 0-1.548-.28-2.158-.525l-.028-.01C7.68 8.71 7.14 8.5 6.5 8.5c-.7 0-1.638.23-2.437.477A19.626 19.626 0 0 0 3 9.342V15.5a.5.5 0 0 1-1 0V.5a.5.5 0 0 1 1 0v.282c.226-.079.496-.17.79-.26C4.606.272 5.67 0 6.5 0c.84 0 1.524.277 2.121.519l.043.018C9.286.788 9.828 1 10.5 1c.7 0 1.638-.23 2.437-.477a19.587 19.587 0 0 0 1.349-.476l.019-.007.004-.002h.001"/></svg></p>
                                </p>
                                <p v-html="comment.content"></p>
                                <p>
                                    <span class="ms-1">{{comment.like}}</span>
                                    <svg @click="likeComment(comment.id)" class="custom-cursor" xmlns="http://www.w3.org/2000/svg" width="25" height="25" viewBox="0 0 512 512"><!--! Font Awesome Pro 6.1.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. --><path d="M96 191.1H32c-17.67 0-32 14.33-32 31.1v223.1c0 17.67 14.33 31.1 32 31.1h64c17.67 0 32-14.33 32-31.1V223.1C128 206.3 113.7 191.1 96 191.1zM512 227c0-36.89-30.05-66.92-66.97-66.92h-99.86C354.7 135.1 360 113.5 360 100.8c0-33.8-26.2-68.78-70.06-68.78c-46.61 0-59.36 32.44-69.61 58.5c-31.66 80.5-60.33 66.39-60.33 93.47c0 12.84 10.36 23.99 24.02 23.99c5.256 0 10.55-1.721 14.97-5.26c76.76-61.37 57.97-122.7 90.95-122.7c16.08 0 22.06 12.75 22.06 20.79c0 7.404-7.594 39.55-25.55 71.59c-2.046 3.646-3.066 7.686-3.066 11.72c0 13.92 11.43 23.1 24 23.1h137.6C455.5 208.1 464 216.6 464 227c0 9.809-7.766 18.03-17.67 18.71c-12.66 .8593-22.36 11.4-22.36 23.94c0 15.47 11.39 15.95 11.39 28.91c0 25.37-35.03 12.34-35.03 42.15c0 11.22 6.392 13.03 6.392 22.25c0 22.66-29.77 13.76-29.77 40.64c0 4.515 1.11 5.961 1.11 9.456c0 10.45-8.516 18.95-18.97 18.95h-52.53c-25.62 0-51.02-8.466-71.5-23.81l-36.66-27.51c-4.315-3.245-9.37-4.811-14.38-4.811c-13.85 0-24.03 11.38-24.03 24.04c0 7.287 3.312 14.42 9.596 19.13l36.67 27.52C235 468.1 270.6 480 306.6 480h52.53c35.33 0 64.36-27.49 66.8-62.2c17.77-12.23 28.83-32.51 28.83-54.83c0-3.046-.2187-6.107-.6406-9.122c17.84-12.15 29.28-32.58 29.28-55.28c0-5.311-.6406-10.54-1.875-15.64C499.9 270.1 512 250.2 512 227z"/></svg>
                                    <span class="me-4 ms-1">{{comment.dis_like}}</span>
                                    <svg @click="disLikeComment(comment.id)" class="custom-cursor" xmlns="http://www.w3.org/2000/svg" width="25" height="25" viewBox="0 0 512 512"><!--! Font Awesome Pro 6.1.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. --><path d="M128 288V64.03c0-17.67-14.33-31.1-32-31.1H32c-17.67 0-32 14.33-32 31.1v223.1c0 17.67 14.33 31.1 32 31.1h64C113.7 320 128 305.7 128 288zM481.5 229.1c1.234-5.092 1.875-10.32 1.875-15.64c0-22.7-11.44-43.13-29.28-55.28c.4219-3.015 .6406-6.076 .6406-9.122c0-22.32-11.06-42.6-28.83-54.83c-2.438-34.71-31.47-62.2-66.8-62.2h-52.53c-35.94 0-71.55 11.87-100.3 33.41L169.6 92.93c-6.285 4.71-9.596 11.85-9.596 19.13c0 12.76 10.29 24.04 24.03 24.04c5.013 0 10.07-1.565 14.38-4.811l36.66-27.51c20.48-15.34 45.88-23.81 71.5-23.81h52.53c10.45 0 18.97 8.497 18.97 18.95c0 3.5-1.11 4.94-1.11 9.456c0 26.97 29.77 17.91 29.77 40.64c0 9.254-6.392 10.96-6.392 22.25c0 13.97 10.85 21.95 19.58 23.59c8.953 1.671 15.45 9.481 15.45 18.56c0 13.04-11.39 13.37-11.39 28.91c0 12.54 9.702 23.08 22.36 23.94C456.2 266.1 464 275.2 464 284.1c0 10.43-8.516 18.93-18.97 18.93H307.4c-12.44 0-24 10.02-24 23.1c0 4.038 1.02 8.078 3.066 11.72C304.4 371.7 312 403.8 312 411.2c0 8.044-5.984 20.79-22.06 20.79c-12.53 0-14.27-.9059-24.94-28.07c-24.75-62.91-61.74-99.9-80.98-99.9c-13.8 0-24.02 11.27-24.02 23.99c0 7.041 3.083 14.02 9.016 18.76C238.1 402 211.4 480 289.9 480C333.8 480 360 445 360 411.2c0-12.7-5.328-35.21-14.83-59.33h99.86C481.1 351.9 512 321.9 512 284.1C512 261.8 499.9 241 481.5 229.1z"/></svg>
                                </p>

                                <p v-if="comment.comments_reply.length != 0" @click="showReplyComment = !showReplyComment" class="text-danger custom-cursor d-inline">پاسخ ها ({{comment.comments_reply.length}})</p>
                                <svg v-if="showReplyComment & comment.comments_reply.length != 0" xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-arrow-up-short text-danger" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M8 12a.5.5 0 0 0 .5-.5V5.707l2.146 2.147a.5.5 0 0 0 .708-.708l-3-3a.5.5 0 0 0-.708 0l-3 3a.5.5 0 1 0 .708.708L7.5 5.707V11.5a.5.5 0 0 0 .5.5z"/></svg>
                                <svg v-if="!showReplyComment & comment.comments_reply.length != 0" xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-arrow-down-short text-danger" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M8 4a.5.5 0 0 1 .5.5v5.793l2.146-2.147a.5.5 0 0 1 .708.708l-3 3a.5.5 0 0 1-.708 0l-3-3a.5.5 0 1 1 .708-.708L7.5 10.293V4.5A.5.5 0 0 1 8 4z"/></svg>

                                <div v-if="showReplyComment" v-for="cum in comment.comments_reply" class="border me-3 p-2 my-4">
                                    <p class="d-flex">
                                        <p class="ms-3 text-end"><router-link :to="`/user/${cum.username_slug}`">{{cum.username}}</router-link></p>
                                        <p @click="takeIdReply(cum.id)" title="ریپلای" class="me-auto custom-cursor" data-bs-toggle="modal" data-bs-target="#staticBackdrop4"><svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-reply-fill" viewBox="0 0 16 16"><path d="M5.921 11.9 1.353 8.62a.719.719 0 0 1 0-1.238L5.921 4.1A.716.716 0 0 1 7 4.719V6c1.5 0 6 0 7 8-2.5-4.5-7-4-7-4v1.281c0 .56-.606.898-1.079.62z"/></svg></p>
                                        <p @click="takeId(cum.id)" title="گزارش تخلف" class="me-2 custom-cursor" data-bs-toggle="modal" data-bs-target="#staticBackdrop3"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-flag-fill" viewBox="0 0 16 16"><path d="M14.778.085A.5.5 0 0 1 15 .5V8a.5.5 0 0 1-.314.464L14.5 8l.186.464-.003.001-.006.003-.023.009a12.435 12.435 0 0 1-.397.15c-.264.095-.631.223-1.047.35-.816.252-1.879.523-2.71.523-.847 0-1.548-.28-2.158-.525l-.028-.01C7.68 8.71 7.14 8.5 6.5 8.5c-.7 0-1.638.23-2.437.477A19.626 19.626 0 0 0 3 9.342V15.5a.5.5 0 0 1-1 0V.5a.5.5 0 0 1 1 0v.282c.226-.079.496-.17.79-.26C4.606.272 5.67 0 6.5 0c.84 0 1.524.277 2.121.519l.043.018C9.286.788 9.828 1 10.5 1c.7 0 1.638-.23 2.437-.477a19.587 19.587 0 0 0 1.349-.476l.019-.007.004-.002h.001"/></svg></p>
                                    </p>
                                    <p v-html="cum.content"></p>
                                    <p>
                                        <span class="ms-1">{{cum.like}}</span>
                                        <svg @click="likeComment(cum.id)" class="custom-cursor" xmlns="http://www.w3.org/2000/svg" width="25" height="25" viewBox="0 0 512 512"><!--! Font Awesome Pro 6.1.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. --><path d="M96 191.1H32c-17.67 0-32 14.33-32 31.1v223.1c0 17.67 14.33 31.1 32 31.1h64c17.67 0 32-14.33 32-31.1V223.1C128 206.3 113.7 191.1 96 191.1zM512 227c0-36.89-30.05-66.92-66.97-66.92h-99.86C354.7 135.1 360 113.5 360 100.8c0-33.8-26.2-68.78-70.06-68.78c-46.61 0-59.36 32.44-69.61 58.5c-31.66 80.5-60.33 66.39-60.33 93.47c0 12.84 10.36 23.99 24.02 23.99c5.256 0 10.55-1.721 14.97-5.26c76.76-61.37 57.97-122.7 90.95-122.7c16.08 0 22.06 12.75 22.06 20.79c0 7.404-7.594 39.55-25.55 71.59c-2.046 3.646-3.066 7.686-3.066 11.72c0 13.92 11.43 23.1 24 23.1h137.6C455.5 208.1 464 216.6 464 227c0 9.809-7.766 18.03-17.67 18.71c-12.66 .8593-22.36 11.4-22.36 23.94c0 15.47 11.39 15.95 11.39 28.91c0 25.37-35.03 12.34-35.03 42.15c0 11.22 6.392 13.03 6.392 22.25c0 22.66-29.77 13.76-29.77 40.64c0 4.515 1.11 5.961 1.11 9.456c0 10.45-8.516 18.95-18.97 18.95h-52.53c-25.62 0-51.02-8.466-71.5-23.81l-36.66-27.51c-4.315-3.245-9.37-4.811-14.38-4.811c-13.85 0-24.03 11.38-24.03 24.04c0 7.287 3.312 14.42 9.596 19.13l36.67 27.52C235 468.1 270.6 480 306.6 480h52.53c35.33 0 64.36-27.49 66.8-62.2c17.77-12.23 28.83-32.51 28.83-54.83c0-3.046-.2187-6.107-.6406-9.122c17.84-12.15 29.28-32.58 29.28-55.28c0-5.311-.6406-10.54-1.875-15.64C499.9 270.1 512 250.2 512 227z"/></svg>
                                        <span class="me-4 ms-1">{{cum.dis_like}}</span>
                                        <svg @click="disLikeComment(cum.id)" class="custom-cursor" xmlns="http://www.w3.org/2000/svg" width="25" height="25" viewBox="0 0 512 512"><!--! Font Awesome Pro 6.1.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. --><path d="M128 288V64.03c0-17.67-14.33-31.1-32-31.1H32c-17.67 0-32 14.33-32 31.1v223.1c0 17.67 14.33 31.1 32 31.1h64C113.7 320 128 305.7 128 288zM481.5 229.1c1.234-5.092 1.875-10.32 1.875-15.64c0-22.7-11.44-43.13-29.28-55.28c.4219-3.015 .6406-6.076 .6406-9.122c0-22.32-11.06-42.6-28.83-54.83c-2.438-34.71-31.47-62.2-66.8-62.2h-52.53c-35.94 0-71.55 11.87-100.3 33.41L169.6 92.93c-6.285 4.71-9.596 11.85-9.596 19.13c0 12.76 10.29 24.04 24.03 24.04c5.013 0 10.07-1.565 14.38-4.811l36.66-27.51c20.48-15.34 45.88-23.81 71.5-23.81h52.53c10.45 0 18.97 8.497 18.97 18.95c0 3.5-1.11 4.94-1.11 9.456c0 26.97 29.77 17.91 29.77 40.64c0 9.254-6.392 10.96-6.392 22.25c0 13.97 10.85 21.95 19.58 23.59c8.953 1.671 15.45 9.481 15.45 18.56c0 13.04-11.39 13.37-11.39 28.91c0 12.54 9.702 23.08 22.36 23.94C456.2 266.1 464 275.2 464 284.1c0 10.43-8.516 18.93-18.97 18.93H307.4c-12.44 0-24 10.02-24 23.1c0 4.038 1.02 8.078 3.066 11.72C304.4 371.7 312 403.8 312 411.2c0 8.044-5.984 20.79-22.06 20.79c-12.53 0-14.27-.9059-24.94-28.07c-24.75-62.91-61.74-99.9-80.98-99.9c-13.8 0-24.02 11.27-24.02 23.99c0 7.041 3.083 14.02 9.016 18.76C238.1 402 211.4 480 289.9 480C333.8 480 360 445 360 411.2c0-12.7-5.328-35.21-14.83-59.33h99.86C481.1 351.9 512 321.9 512 284.1C512 261.8 499.9 241 481.5 229.1z"/></svg>
                                    </p>
                                </div>

                            </div>

                        </div>
                    </section>
                </div>
            </div>
        </div>
    </div>

    <div v-if="return404" class="PageNotFound bg-dark">
        <div class="container text-center p-5">
            <h1 class="text-muted" id="text-404">404</h1>
            <p class="text-light">صفحه مورد نظر شما یافت نشد.</p>
            <hr class="text-white">    
        </div>
    </div>
</template>


<script>
import { ref, onMounted, watch } from "vue";
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'
import Swal from 'sweetalert2'
import { useMeta } from 'vue-meta'

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

        let book = ref('')

        let relatedBooks = ref('')

        let author_books = ref('')


        let slugForRate = ref('')
        let rate_number = ref('')

        let comments = ref('')
        let commentContent = ref('')

        let return404 = ref(false)

        let cause = ref('')
        let id = ref('')

        let idReply = ref(0)

        let showReplyComment = ref(false)

        function getData(sl){
            document.body.scrollTop = 0; // For Safari
            document.documentElement.scrollTop = 0;
            if (sl){
                slug.value = sl  
            }else{
                slug.value = route.params.slug
            }
            axios
            .post('ShowSingleBook/', {
                slug: slug.value
            })
            .then(response => {
                book.value = response.data.data
                relatedBooks.value = response.data.related_books_data
                author_books.value = response.data.author_books_data
                return404.value = false
                document.title  = book.value[0].title
            })
            .catch(error => {
                return404.value = true
                console.log(error.response);
            })
        }
        getData()
        
        // for meta tags
        onMounted(() => {
            setTimeout(setMetaDescription, 1000)
            function setMetaDescription(){

                let content = ref(document.getElementById('content_book').innerText)
                content.value = content.value.substring(0,200)
                content.value = content.value.replace(/(\r\n|\n|\r)/gm, "");
                document.querySelector('meta[name="description"]').setAttribute("content", content.value);
                document.querySelector('meta[name="og:description"]').setAttribute("content", content.value);
            }
        })

        // take the book slug that user want to rate it
        function takeSlug(sl){
            slugForRate.value = sl
        }

        // take the comment id that user want to report it
        function takeId(idd){
            id.value = idd
        }
        
        // take the comment id that user want to reply it
        function takeIdReply(idd){
            idReply.value = idd
        }

        // making rate
        function sendRate(number, sl){
            rate_number.value = number

            // if sl is defined, so user want to rate to book with detail
            if(sl){

                axios
                .post('MakeRate/', {
                    user_score: rate_number.value,
                    slug: sl
                })
                .then(response => {
                    let target = ref(book.value.filter((r) => r.slug == sl))
                    target.value[0].user_score = rate_number.value
                })
                .catch(error => {
                    if(error.response.status == 401){
                        router.push('/login')
                    }
                })
            
            // if sl isn't defined, so user want to rate to one of the related book
            }else{

                axios
                .post('MakeRate/', {
                    user_score: rate_number.value,
                    slug: slugForRate.value
                })
                .then(response => {
                    let target = ref(relatedBooks.value.filter((r) => r.slug == slugForRate.value))
                    target.value[0].user_score = rate_number.value
                })
                .catch(error => {
                    if(error.response.status == 401){
                        router.push('/login')
                    }
                })
            }
            document.getElementById('close-modal').click()
            document.getElementById('close-modal2').click()

            
        }

        function addOrRemoveFromReadlist(sl){
			axios
			.post('AddOrRemoveFromReadlist/', {
				'slug': sl
			})
			.then(response => {
                let target = ref(relatedBooks.value.filter((r) => r.slug == sl))
                if(target.value.length != 0){
                    target.value[0].in_readlist = !target.value[0].in_readlist
                } else {
                    let target = ref(book.value.filter((r) => r.slug == sl))
                    target.value[0].in_readlist = !target.value[0].in_readlist
                }
			})
			.catch(error => {
				if(error.response.status == 401){
					router.push('/login')
				}
				console.log(error.response);
			})
		}


        function getComments(){
            axios
			.post('ShowComment/', {
                slug: slug.value
            })
			.then(response => {
				comments.value = response.data.data
			})
			.catch(error => {
				console.log(error.response);
			})
        }
        getComments()


        function likeComment(id){
            axios
			.post('LikeComment/', {
                id: id
            })
			.then(response => {
                if(response.data.status == 'you like this comment before'){
                    Swal.fire({
                        icon: 'info',
                        title: 'شما این کامنت را قبلا لایک کردید.',
                        backdrop: false,
                        timer: 1500,
                        showConfirmButton: false,
                        position: 'top',
                    })
                } else if(response.data.status == 'you changed your status from dis_like to like'){
                    Swal.fire({
                        icon: 'success',
                        title: 'شما قبلا این کامنت را دیس لایک و اکنون لایک کردید..',
                        text: '',
                        backdrop: false,
                        timer: 1500,
                        showConfirmButton: false,
                        position: 'top',
                    })

                    let target = ref(comments.value.filter((r) => r.id == id))
                    if(target.value.length != 0){
                        target.value[0].like += 1
                        target.value[0].dis_like -= 1
                    }

                } else if(response.data.status == 'OK'){
                    Swal.fire({
                        icon: 'success',
                        title: 'شما این کامنت را لایک کردید.',
                        backdrop: false,
                        timer: 1500,
                        showConfirmButton: false,
                        position: 'top',
                    })

                    let target = ref(comments.value.filter((r) => r.id == id))
                    if(target.value.length != 0){
                        target.value[0].like += 1
                    }
                }
			})
			.catch(error => {
				if(error.response.status == 401){
					router.push('/login')
				}
				console.log(error.response);
			})
        }


        function disLikeComment(id){
            axios
			.post('DisLikeComment/', {
                id: id
            })
			.then(response => {
                if(response.data.status == 'you dis_like this comment before'){
                    Swal.fire({
                        icon: 'info',
                        title: 'شما این کامنت را قبلا دیس لایک کردید.',
                        backdrop: false,
                        timer: 1500,
                        showConfirmButton: false,
                        position: 'top',
                    })
                } else if(response.data.status == 'you changed your status from like to dis_like'){
                    Swal.fire({
                        icon: 'success',
                        title: 'شما قبلا این کامنت را لایک و اکنون دیس لایک کردید.',
                        backdrop: false,
                        timer: 1500,
                        showConfirmButton: false,
                        position: 'top',
                    })

                    let target = ref(comments.value.filter((r) => r.id == id))
                    if(target.value.length != 0){
                        target.value[0].dis_like += 1
                        target.value[0].like -= 1
                    }
                } else if(response.data.status == 'OK'){
                    Swal.fire({
                        icon: 'success',
                        title: 'شما این کامنت را دیس لایک کردید.',
                        backdrop: false,
                        timer: 1500,
                        showConfirmButton: false,
                        position: 'top',
                    })

                    let target = ref(comments.value.filter((r) => r.id == id))
                    if(target.value.length != 0){
                        target.value[0].dis_like += 1
                    }

                }

			})
			.catch(error => {
				if(error.response.status == 401){
					router.push('/login')
				}
				console.log(error.response);
			})
        }


        function makeComment(){
            axios
			.post('MakeComment/', {
                content: commentContent.value,
                slug: slug.value,
                id: idReply.value,
            })
			.then(response => {
                commentContent.value = ''
                idReply.value = 0
                getComments()

				Swal.fire({
                    icon: 'success',
                    title: 'دیدگاه شما ثبت شد.',
                    backdrop: false,
                    timer: 1500,
                    showConfirmButton: false,
                })
			})
			.catch(error => {
                idReply.value = 0
				if(error.response.status == 400){
                    Swal.fire({
                        icon: 'warning',
                        title: 'لطفا متن دیدگاه خود را وارد کنید.',
                        timer: 2500,
                        showConfirmButton: false,
                    })
                }
			})
            document.getElementById('close-modal4').click()
        }


        function report(){
            axios
			.post('AddReport/', {
				cause: cause.value,
                id: id.value,
			})
			.then(response => {
				Swal.fire({
                    icon: 'success',
                    title: 'گزارش تخلف با موفقیت ثبت شد.',
                    timer: 1500,
                    showConfirmButton: false,
                })
                cause.value = ''
			})
			.catch(error => {
                if(error.response.status == 401){
					router.push('/login')
				}

                if(error.response.status == 400){
					Swal.fire({
                        icon: 'warning',
                        title: 'لطفا قسمت توضیحات را به درستی پر کنید.',
                        timer: 1500,
                        showConfirmButton: false,
                    })
				}
				console.log(error.response);
			})
            document.getElementById('close-modal3').click()
        }



        function largerImage(){
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


        // comment filter
        let upToDown = ref(true)
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

        // hot : comment with more reply
        function filterHottest(){
            upToDown.value = !upToDown.value
            if(upToDown.value){
                comments.value.sort(function(a , b) {
                    return b.comments_reply.length - a.comments_reply.length;
                })
            } else {
                comments.value.sort(function(a , b) {
                    return a.comments_reply.length - b.comments_reply.length;
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


        // meta information
        useMeta({
            robots: "index, follow",
            keywords: "کتاب خوار, کتاب, نویسنده, نقد کتاب, کتابخانه, دسته بندی های کتاب, برترین کتاب ها",
            googlebot: "index, follow",
            author: "امین مهری",
            owner: "امین مهری",
            canonical: `https://bookeater.ir/book/${route.params.slug}`,
            'og:type': `${route.params.slug}-bookeater`,
            'og:title': "bookeater",
            'og:site_name': "کتاب خوار",
            'og:url': `https://bookeater.ir/book/${route.params.slug}`,
            'og:image': "https://bookeater.ir/media/image.jpg",
            'twitter:title': "کتاب خوار",
            'twitter:description': "کتاب هایی با بیشترین نمره را در سایت کتاب خوار گرفته اند. شما نیز میتوانید یکی از رای دهندگان به این کتاب باشید.",
            'twitter:site': "https://twitter.com/aminem_mehri",
            'twitter:card': "Summary Card",
            'twitter:image': "https://bookeater.ir/media/image.jpg",
        });

        return {
            largerImage,
            book,
            relatedBooks,
            author_books,
            slug,
            comments,
            commentContent,
            swiperOptions,
            return404,
            cause,
            showReplyComment,
            upToDown,
            getData,
            sendRate,
            takeSlug,
            addOrRemoveFromReadlist,
            getComments,
            likeComment,
            disLikeComment,
            makeComment,
            report,
            takeId,
            takeIdReply,
            filterLike,
            filterDisLike,
            filterHottest,
            filterDate,
        };
    },
};
</script>


<style>
.single-category{   
    border-left: 1px solid rgb(0, 0, 0);
    border-right: 1px solid rgb(151, 151, 151);
    background-color: #eee;
}
.author-link:hover{
    color: black !important;
    transition-duration: 0.25s;
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

.custom-cursor {
    cursor: pointer;
}

/* Swal style */
.swal2-popup {
    font-size: 0.8rem;
    direction: rtl;
}
</style>