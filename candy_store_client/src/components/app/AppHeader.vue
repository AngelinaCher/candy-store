<template>
  <div class="app-header">

    <nav class="app-header_nav">

      <router-link class="app-header_nav__logo" to="/">
        Карамелька
      </router-link>

      <div class="app-header_nav__menu">
        <b-dropdown id="dropdown-left" text="Каталог" class="catalog-dropdown">
          <b-dropdown-item href="#">Батончики</b-dropdown-item>
          <b-dropdown-item href="#">Шоколад</b-dropdown-item>
        </b-dropdown>
      </div>

      <div class="app-header_nav__search">
        <b-form-input 
          placeholder="Поиск по товарам" 
          class="custom-input"
        ></b-form-input>
      </div>

      <router-link class="app-header_nav__cart" to="/">
        <div>
          <img src="../../assets/icons/cart.svg" alt="">
        </div>
        <div class="app-header_nav__account_text">
          Корзина
        </div>
      </router-link>

      <router-link class="app-header_nav__account" to="/">
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
export default {
  name: "AppHeader",
}
</script>

<style>

</style>