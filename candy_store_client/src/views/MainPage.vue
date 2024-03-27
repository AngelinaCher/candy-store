<template>
  <div class="main-page">
    <Bannner/>
    <Categories />
  </div>
</template>

<script>
import Bannner from "../components/main-page/Banner.vue";
import Categories from "../components/main-page/Categories.vue";

export default {
  name: "MainPage",
  components: {
    Bannner,
    Categories,
  }
}
</script>