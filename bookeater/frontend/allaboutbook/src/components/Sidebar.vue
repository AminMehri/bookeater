<template>
    <div class="col-sm-4 col-md-3 col-lg-2">
        <div class="d-flex flex-column flex-shrink-0 p-3 text-white bg-dark sidenav">

            <router-link to="/author-panel" class="d-flex align-items-center mb-3 mb-md-0 text-white text-decoration-none">
                
                <span class="fs-4">کتاب خوار</span>
            </router-link>
            
            <hr>

            <ul class="nav nav-pills flex-column">

                <li class="nav-item text-dark">

                    <button class="accordion-button p-2 bg-white text-dark nav-link align-items-center collapsed1" type="button" data-bs-toggle="collapse" data-bs-target="#dashboard-collapse1">
                            کتاب ها
                    </button>
                    <div class="collapse" id="dashboard-collapse1">
                        <ul class="btn-toggle-nav list-unstyled fw-normal pb-1 small">
                            <li><router-link to="/author-panel/books" class=" text-white" >کتاب ها</router-link></li>
                            <li><router-link to="/author-panel/add-book/new-book" class=" text-white" >اضافه کردن</router-link></li>
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
                            <li><router-link to="/author-panel/add-author/new-author" class=" text-white" >اضافه کردن</router-link></li>
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
                            <li><router-link to="/author-panel/add-category/new-category" class=" text-white" >اضافه کردن</router-link></li>
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
                            <li><router-link to="/author-panel/add-reviewed-book/new-reviewed-book" class=" text-white" >اضافه کردن</router-link></li>
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
                            <li><router-link to="/author-panel/add-news/new-news" class=" text-white" >اضافه کردن</router-link></li>
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
        </div>
    </div>
</template>





<script>

export default {
    
    setup() {
    
        return {
            
        }

    }
}
</script>