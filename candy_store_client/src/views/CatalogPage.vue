<template>
  <div class="catalog-page">

    <div class="cart-page_header">
      <h1>{{ headerProduct }}</h1>
      <span style="padding-top: 50px; font-size: 12px; color: #aeaeae;">{{ products.length }} товаров</span>
    </div>

    <div class="catalog-page_content">

      <div class="catalog-page_categories">
        <div
            class="catalog-page_categories__category"
            v-for="cat in categories"
            :key="cat['category_id']"
            @click="getProductsByCategories(cat)"
        >
          <p class="catalog-page_categories__category_name">{{ cat["category_name"] }}</p>
        </div>
      </div>

      <div class="catalog-page_products">
        <div
            class="catalog-page_products__product"
            v-for="product in products"
            :key="product['product_id']"
        >
          <router-link :to="{ name: 'ProductPage', params: { productSlug: `${product['slug']}` }}">
            <img
                :src="product['image_path']"
                :alt="product['product_name']"
                class="catalog-page_products__product_img"
            >
            <h2 class="catalog-page_products__product_name"> {{ product["product_name"] }} </h2>
            <p class="catalog-page_products__product_price">{{ product["unit_price"] }} ₽</p>
          </router-link>
          <b-button class="custom-button">В корзину</b-button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "CatalogPage",
  props: ["productName"],
  data() {
    return {
      headerCategory: "",
      categories: [],
      products: [],
      headerProduct: "",
    }
  },
  mounted() {
    document.title = "Каталог | Карамелька ";
    this.getProductsByCategories(this.productName);
    this.getAllCategories();
  },
  watch: {
    productName(newVal, oldVal) {
      this.getProductsByCategories(newVal);
    }
  },
  methods: {
    getDataProps(productNameProps) {
      return productNameProps.split("/");
    },
    async getProductsByCategories(productData) {
      let url = "";
      if (typeof productData === "object") {
        url = `http://127.0.0.1:8000/api/v1/products?category_id=${Number(productData["category_id"])}`
      } else {
        const dataProps = this.getDataProps(productData);
        url = `http://127.0.0.1:8000/api/v1/products?category_id=${dataProps[0]}`
      }
      await axios
          .get(url)
          .then(response => {
            this.headerProduct = response.data[0]["category_name"];
            this.products = response.data;
          })
          .catch(err => console.log(err))
    },
    async getAllCategories() {
      await axios
          .get("http://127.0.0.1:8000/api/v1/categories")
          .then(response => {
            this.categories = response.data;
          })
          .catch(err => console.log(err))
    }
  },
}
</script>