<template>
    <div class="row g-0">

        <div class="col-sm-4 col-md-3 col-lg-2">
            <sidebar class="d-flex flex-column flex-shrink-0 p-3 text-white bg-dark sidenav">

                <a href="/" class="d-flex align-items-center mb-3 mb-md-0 text-white text-decoration-none">
                    
                    <span class="fs-4">کتاب خوار</span>
                </a>
                
                <hr>

                <ul class="nav nav-pills flex-column">

                    <li class="nav-item text-dark">

                        <button class="accordion-button p-2 bg-white text-dark nav-link align-items-center collapsed1" type="button" data-bs-toggle="collapse" data-bs-target="#dashboard-collapse1">
                                کتاب ها
                        </button>
                        <div class="collapse" id="dashboard-collapse1">
                            <ul class="btn-toggle-nav list-unstyled fw-normal pb-1 small">
                                <li><router-link to="/author-panel/books" class=" text-white" >کتاب ها</router-link></li>
                                <li><router-link to="/author-panel/add-book" class=" text-white" >اضافه کردن</router-link></li>
                            </ul>
                        </div>
                    </li>

                    <li class="nav-item text-dark">

                        <button class="accordion-button p-2 bg-white text-dark nav-link align-items-center  collapsed2" type="button" data-bs-toggle="collapse" data-bs-target="#dashboard-collapse2">
                                نویسنده ها
                        </button>
                        <div class="collapse" id="dashboard-collapse2">
                            <ul class="btn-toggle-nav list-unstyled fw-normal pb-1 small">
                                <li><router-link to="/author-panel/authors" class=" text-white" >نویسنده ها</router-link></li>
                                <li><router-link to="/author-panel/add-author" class=" text-white" >اضافه کردن</router-link></li>
                            </ul>
                        </div>
                    </li>

                    <li class="nav-item text-dark">

                        <button class="accordion-button p-2 bg-white text-dark nav-link align-items-center  collapsed3" type="button" data-bs-toggle="collapse" data-bs-target="#dashboard-collapse3">
                                دسته بندی ها
                        </button>
                        <div class="collapse" id="dashboard-collapse3">
                            <ul class="btn-toggle-nav list-unstyled fw-normal pb-1 small">
                                <li><router-link to="/author-panel/categories" class=" text-white" >دسته بندی ها</router-link></li>
                                <li><router-link to="/author-panel/add-category" class=" text-white" >اضافه کردن</router-link></li>
                            </ul>
                        </div>
                    </li>

                    <li class="nav-item text-dark">

                        <button class="accordion-button p-2 bg-white text-dark nav-link align-items-center  collapsed4" type="button" data-bs-toggle="collapse" data-bs-target="#dashboard-collapse4">
                                نقد ها
                        </button>
                        <div class="collapse" id="dashboard-collapse4">
                            <ul class="btn-toggle-nav list-unstyled fw-normal pb-1 small">
                                <li><router-link to="/author-panel/reviewed-books" class=" text-white" >نقد ها</router-link></li>
                                <li><router-link to="/author-panel/add-reviewed-book" class=" text-white" >اضافه کردن</router-link></li>
                            </ul>
                        </div>
                    </li>

                    <li class="nav-item text-dark">

                        <button class="accordion-button p-2 bg-white text-dark nav-link align-items-center  collapsed5" type="button" data-bs-toggle="collapse" data-bs-target="#dashboard-collapse5">
                                خبر ها
                        </button>
                        <div class="collapse" id="dashboard-collapse5">
                            <ul class="btn-toggle-nav list-unstyled fw-normal pb-1 small">
                                <li><router-link to="/author-panel/news" class=" text-white" >خبر ها</router-link></li>
                                <li><router-link to="/author-panel/add-news" class=" text-white" >اضافه کردن</router-link></li>
                            </ul>
                        </div>
                    </li>

                    <li class="nav-item text-dark">

                        <button class="accordion-button p-2 bg-white text-dark nav-link align-items-center  collapsed6" type="button" data-bs-toggle="collapse" data-bs-target="#dashboard-collapse6">
                                قصار ها
                        </button>
                        <div class="collapse" id="dashboard-collapse6">
                            <ul class="btn-toggle-nav list-unstyled fw-normal pb-1 small">
                                <li><router-link to="/author-panel/quotes" class=" text-white" >قصار ها</router-link></li>
                                <li><router-link to="/author-panel/add-quote" class=" text-white" >اضافه کردن</router-link></li>
                            </ul>
                        </div>
                    </li>

                </ul>
                <hr>
            </sidebar>
        </div>


        <div class="col-sm-8 col-md-9 col-lg-10 p-3 mt-3">
            <h3 class="text-center">اضافه کردن نقل قول</h3>
            <div class="row g-3 border p-4">

                <div class="col-md-6">
                    <label for="inputAuthor" class="form-label">نویسنده</label>
                    <input type="text" class="form-control" id="inputAuthor">
                </div>

                <div class="col-12">
                    <label for="inputDescription" class="form-label">توضیحات</label>
                    <textarea class="form-control" id="inputDescription" rows="6"></textarea>
                </div>

                <div class="col-md-6">
                    <div class="input-group mb-3 align-items-center">
                        <label for="inputThumbnail" class="form-label ms-3">عکس بند انگشتی نویسنده:</label>
                        <input type="file" class="form-control" id="inputThumbnail">
                    </div>
                </div>

                <div class="col-12">
                    <button class="btn btn-primary">ارسال به ادمین</button>
                </div>
            </div>
        </div>
        
    </div>
</template>