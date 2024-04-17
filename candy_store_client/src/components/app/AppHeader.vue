<template>
  <div class="app-header">

    <nav class="app-header_nav">

      <router-link class="app-header_nav__logo" to="/">
        Карамелька
      </router-link>

      <div class="app-header_nav__menu">
        <b-dropdown id="dropdown-left" text="Каталог" class="catalog-dropdown">
          <b-dropdown-item v-for="cat in categories" :key="cat['category_id']">
            <router-link
                :to="{ name: 'CatalogPage', params: { productName: `${cat['category_id']}/${cat['slug']}` }}"
                style="text-decoration: none; color: #000000;"
            >{{ cat["category_name"] }}</router-link>
          </b-dropdown-item>
        </b-dropdown>
      </div>

      <div class="app-header_nav__search">
        <b-form-input
            placeholder="Поиск по товарам"
            class="custom-input"
        ></b-form-input>
      </div>

      <router-link class="app-header_nav__cart" to="/cart">
        <div>
          <img src="../../assets/icons/cart.svg" alt="">
        </div>
        <div class="app-header_nav__account_text">
          Корзина
        </div>
      </router-link>

      <router-link class="app-header_nav__account" to="/account">
        <div class="">
          <img src="../../assets/icons/account.svg" alt="">
        </div>
        <div class="app-header_nav__account_text">
          Аккаунт
        </div>
      </router-link>

    </nav>

  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "AppHeader",
  data() {
    return {
      categories: [],
    }
  },
  mounted() {
    this.getCategories();
  },
  methods: {
    async getCategories() {
      await axios
          .get("http://127.0.0.1:8000/api/v1/categories")
          .then(response => {
            this.categories = response.data;
          })
          .catch(err => {
            console.log(err);
          })
    }
  },
}
</script>

<style>

</style>