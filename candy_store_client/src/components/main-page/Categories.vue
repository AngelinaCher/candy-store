<template>
  <div class="main-page_categories">
    <router-link
        class="main-page_categories_category"
        v-for="cat in categories"
        :key="cat['category_id']"
        :to="{ name: 'CatalogPage', params: { productName: `${cat['category_id']}/${cat['slug']}` }}"
    >
      <h1>{{ cat["category_name"] }}</h1>
      <p>{{ cat["desc"] }}</p>
<!--      <img :src="require(`../../assets/imgs/${cat['slug']}.png`)" :alt="cat['slug']">-->
    </router-link>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Categories",
  data() {
    return {
      categories: [],
    }
  },
  mounted() {
    this.getAllCategories();
  },
  methods: {
    async getAllCategories() {
      await axios
          .get("http://127.0.0.1:8000/api/v1/categories")
          .then(response => {
            this.categories = response.data;
          })
          .catch(err => console.log(err))
    },
  }
}
</script>

