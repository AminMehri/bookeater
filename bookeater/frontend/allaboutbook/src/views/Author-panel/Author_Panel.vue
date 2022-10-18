<template>
    <div class="row g-0">

        <Sidebar />


        <div class="col-sm-8 col-md-9 col-lg-10 text-center">
            <h3 class="alert-info p-4 mt-3">به پنل نویسندگان کتاب خوار خوش آمدید</h3>
        </div>
    </div>
      
</template>

<script>
import Sidebar from '@/components/Sidebar.vue'

export default{
    components: {
        Sidebar
    },
}
</script>


<style>
.sidenav {
  /* height: 100%; */
  /* width: 280px; */
  position: sticky;
  z-index: 5;
  top: 0;
  right: 0;
  background-color: #111;
  overflow-x: hidden;
  padding-top: 20px;
}

@media screen and (max-height: 450px) {
  .sidenav {padding-top: 15px;}
  .sidenav a {font-size: 18px;}
}
</style>