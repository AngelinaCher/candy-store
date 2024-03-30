<template>
  <div class="main-page">
    <Banner/>
    <Categories/>
    <NewProducts/>
    <RecommendedProducts/>
  </div>
</template>

<script>
import Banner from "../components/main-page/Banner.vue";
import Categories from "../components/main-page/Categories.vue";
import NewProducts from "../components/main-page/NewProducts.vue";
import RecommendedProducts from "../components/main-page/RecommendedProducts.vue";


export default {
  name: "MainPage",
  components: {
    Banner,
    Categories,
    NewProducts,
    RecommendedProducts,
  },
  mounted() {
    document.title = "Главная | Карамелька "
  },
}
</script>