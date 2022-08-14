<template>
    <header class="p-5 bg-dark text-white">
        <div class="container row">

            <div class="col-md-2"></div>
            
            <div class="col-md-4">
                <h1>همه چیز درباره کتاب</h1>
            </div>

            <div class="col-md-2"></div>

            <div class="col-md-4">
                <p>کتاب خوب را خوب بخوانیم</p>
                <p>کتاب بد را بد بخوانیم</p>
            </div>
        </div>
    </header>

    
    <!-- offcanvas -->
    <div class="offcanvas offcanvas-end bg-dark" tabindex="-1" id="offcanvasRight" aria-labelledby="offcanvasRightLabel">
        <div class="offcanvas-header">
            <h5 id="offcanvasRightLabel">Offcanvas right</h5>
            <button type="button" class="btn-close text-reset bg-light" data-bs-dismiss="offcanvas" aria-label="Close"></button>
        </div>
        <div class="offcanvas-body">
            
            <router-link to="/" class="nav-item nav-link text-light fw-bold warning-on-hover">صفحه اصلی</router-link>
            <router-link to="/categories" class="nav-item nav-link text-light fw-bold warning-on-hover">دسته بندی ها</router-link>
            <router-link to="/authors" class="nav-item nav-link text-light fw-bold warning-on-hover">نویسنده ها</router-link>
            <router-link to="/reviewed-books" class="nav-item nav-link text-light fw-bold warning-on-hover">کتابهای نقد شده</router-link>
            <router-link to="/news" class="nav-item nav-link text-light fw-bold warning-on-hover">جدیدترین خبر ها</router-link>

        </div>
    </div>

    

    <nav class="navbar sticky-top navbar-expand-lg navbar-dark bg-dark" id="nav">
        <div class="container-fluid">

            <!-- offcanvas button -->
            <button class="btn btn-outline-secondary" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasRight" aria-controls="offcanvasRight"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-bricks" viewBox="0 0 16 16"><path d="M0 .5A.5.5 0 0 1 .5 0h15a.5.5 0 0 1 .5.5v3a.5.5 0 0 1-.5.5H14v2h1.5a.5.5 0 0 1 .5.5v3a.5.5 0 0 1-.5.5H14v2h1.5a.5.5 0 0 1 .5.5v3a.5.5 0 0 1-.5.5H.5a.5.5 0 0 1-.5-.5v-3a.5.5 0 0 1 .5-.5H2v-2H.5a.5.5 0 0 1-.5-.5v-3A.5.5 0 0 1 .5 6H2V4H.5a.5.5 0 0 1-.5-.5v-3zM3 4v2h4.5V4H3zm5.5 0v2H13V4H8.5zM3 10v2h4.5v-2H3zm5.5 0v2H13v-2H8.5zM1 1v2h3.5V1H1zm4.5 0v2h5V1h-5zm6 0v2H15V1h-3.5zM1 7v2h3.5V7H1zm4.5 0v2h5V7h-5zm6 0v2H15V7h-3.5zM1 13v2h3.5v-2H1zm4.5 0v2h5v-2h-5zm6 0v2H15v-2h-3.5z"/></svg></button>
            <!-- offcanvas button -->

            <router-link class="navbar-brand bg-warning p-1 badge badge-warning fs-3 fw-bold text-dark" to="/">همه چیز درباره کتاب</router-link>

            <button type="button" class="navbar-toggler" data-bs-toggle="collapse" data-bs-target="#navbarCollapse">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarCollapse">
                <div class="navbar-nav me-auto">
                    <router-link v-if="!$store.state.isAuthenticated" to="/login" class="btn btn-outline-secondary nav-item nav-link">ورود به حساب کاربری</router-link>
                    <!-- <router-link v-if="$store.state.isAuthenticated" to="/profile" class="btn btn-outline-secondary nav-item nav-link">پروفایل</router-link> -->

                    <div v-if="$store.state.isAuthenticated" class="dropdown dropdown-menu-start nav-item nav-link">
                        <button class="dropbtn btn btn-outline-secondary">{{username}}</button>
                        <div class="dropdown-content">
                            <router-link to="/profile" class="btn btn-outline-secondary">اطلاعات شخصی</router-link>
                            <router-link :to="`/user/${username}`" class="btn btn-outline-secondary">فعالیت های شما</router-link>
                        </div>
                    </div>
                    <router-link v-if="$store.state.isAuthenticated" to="/readlist" class="btn btn-outline-secondary nav-item nav-link ms-2"><div class="badge bg-warning rounded-pill p-1 ms-1">{{count}}</div>کتاب در صدد خواندن <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-book" viewBox="0 0 16 16"><path d="M1 2.828c.885-.37 2.154-.769 3.388-.893 1.33-.134 2.458.063 3.112.752v9.746c-.935-.53-2.12-.603-3.213-.493-1.18.12-2.37.461-3.287.811V2.828zm7.5-.141c.654-.689 1.782-.886 3.112-.752 1.234.124 2.503.523 3.388.893v9.923c-.918-.35-2.107-.692-3.287-.81-1.094-.111-2.278-.039-3.213.492V2.687zM8 1.783C7.015.936 5.587.81 4.287.94c-1.514.153-3.042.672-3.994 1.105A.5.5 0 0 0 0 2.5v11a.5.5 0 0 0 .707.455c.882-.4 2.303-.881 3.68-1.02 1.409-.142 2.59.087 3.223.877a.5.5 0 0 0 .78 0c.633-.79 1.814-1.019 3.222-.877 1.378.139 2.8.62 3.681 1.02A.5.5 0 0 0 16 13.5v-11a.5.5 0 0 0-.293-.455c-.952-.433-2.48-.952-3.994-1.105C10.413.809 8.985.936 8 1.783z"/></svg></router-link>


                </div>
            </div>
        </div>
    </nav>

</template>

<script>
import { ref, onMounted } from "vue";
import axios from 'axios'
import { useRoute, useRouter } from 'vue-router'



export default {
	setup() {
        const route = useRoute()
        let count = ref('')
        let username = ref('')
    
		return {
			count,
            username
		}

    },
    watch: {
		$route() {
            if(this.$store.state.isAuthenticated){
                axios
                .get('ShowReadList/')
                .then(response => {
                    this.count = response.data.data.length
                    this.username = response.data.username
                })
                .catch(error => {
                    console.log(error.response);
                })
            }
		},

	},


}

</script>


<style scoped>

nav {
  padding: 20px;
}

#nav a.router-link-exact-active {
  color: #42b983 !important;
}

.dropdown {
  position: relative;
  display: inline-block;
}

.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f1f1f1;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
}

.dropdown-content a {
  color: black;
  padding: 12px 10px;
  text-decoration: none;
  display: block;
}

.dropdown-content a:hover {
    background-color: #ddd;
}

.dropdown:hover .dropdown-content {
    display: block;
}

</style>