<template>

    <metainfo>
      <template v-slot:title="{ content }">{{ content }}</template>
    </metainfo>

    <div class="PageNotFound bg-dark">
        <div class="container text-center p-5">
            <h1 class="text-muted" id="text-404">404</h1>
            <p class="text-light">صفحه مورد نظر شما یافت نشد.</p>
            <hr class="text-white">    
        </div>

    </div>
</template>

<script>
import { useMeta } from 'vue-meta'

export default {
    setup(){
        useMeta({
        robots: "noindex, nofollow",
        googlebot: "noindex, nofollow",
    });
    }
}
</script>


<style>
#text-404{
    font-size: clamp(7rem, 40vmin, 20rem);
}
</style>