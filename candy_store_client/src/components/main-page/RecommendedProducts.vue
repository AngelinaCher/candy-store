<template>
  <div class="main-page_new_products">

    <h1>Рекомендуем</h1>

    <div class="main-page_new_products_block">
      <router-link
          class="main-page_new_product"
          v-for="product in recommendProducts"
          :key="product.id"
          :to="{ name: 'ProductPage', params: { productSlug: `${product['slug']}` }}"
      >
        <img :src="product['image_path']" :alt="product['slug']">
        <h2> {{ product["product_name"] }} </h2>
        <p>{{ product["unit_price"] }} ₽</p>
        <b-button class="custom-button">В корзину</b-button>
      </router-link>
    </div>

  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "RecommendedProducts",
  data() {
    return {
      recommendProducts: [],
    }
  },
  mounted() {
    this.getAllProducts();
  },
  methods: {
    async getAllProducts() {
      await axios
          .get("http://127.0.0.1:8000/api/v1/products")
          .then(response => {
            this.recommendProducts = response.data.slice(5, 10);
          })
          .catch(err => console.log(err))
    },
  },

}
</script>