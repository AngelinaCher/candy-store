<template>
  <div class="product-page">

    <div class="product-page_content">
      <div class="product-page__image">
        <img :src="product['image_path']" :alt="product['slug']">
      </div>
      <div class="product-page_info">
        <div class="product-page_info__header">
          {{ product["product_name"] }}
        </div>
        <div class="product-page_info__desc">
          {{ product["description"] }}
        </div>
        <div class="product-page_info__price">
          {{ product["unit_price"] }} ₽
        </div>
        <div class="product-page_info__actions">
          <div class="product-page_info__actions_add">
            <div class="cart-page_content__items_amount__sign">
              <img src="../assets/icons/minus.svg" alt="minus" @click="decreaseQuantity">
            </div>

            <div class="cart-page_content__items_amount__amount">{{ quantity }}</div>

            <div class="cart-page_content__items_amount__sign">
              <img src="../assets/icons/plus.svg" alt="plus" @click="increaseQuantity">
            </div>
          </div>
          <div class="product-page_info__actions__add_to_card">
            <b-button class="custom-button" @click="addToCart(product['product_id'])">В корзину</b-button>
          </div>
        </div>
      </div>
    </div>

    <RecommendedProducts/>
  </div>
</template>

<script>
import axios from "axios";

import RecommendedProducts from "../components/main-page/RecommendedProducts.vue";


export default {
  name: "ProductPage",
  props: ["productSlug"],
  components: {
    RecommendedProducts,
  },
  data() {
    return {
      product: {},
      quantity: 1,
    }
  },
  watch: {
    '$route'() {
      this.getProduct();
    }
  },
  created() {
    this.getProduct();
  },
  methods: {
    async getProduct() {
      await axios
          .get(`http://127.0.0.1:8000/api/v1/products/${this.productSlug}/`)
          .then(response => {
            this.product = response.data;
          })
          .catch(err => console.log(err))
    },
    async addToCart(productId) {
      if (this.$store.state.isAuthenticated) {
        await axios
            .post(
                "http://127.0.0.1:8000/api/v1/cart/add/",
                {"product_id": productId, "product_quantity": this.quantity}
            )
            .then(response => console.log(response))
            .catch(err => console.log(err))
      } else {
        const toPath = "/login";
        this.$router.push(toPath);
      }
    },
    decreaseQuantity() {
      if (this.quantity > 1) {
        this.quantity = this.quantity - 1;
      }
    },
    increaseQuantity() {
      this.quantity++;
    },
  },
}
</script>