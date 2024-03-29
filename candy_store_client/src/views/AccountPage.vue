<template>
  <div class="account-page">
    <div class="cart-page_header">
      <h1>Личный кабинет</h1>
    </div>


    <b-tabs pills card vertical class="account-page_tabs">

      <b-tab active class="account-page_tabs__tab">
        <template #title>
        <span class="d-flex align-items-center">
          <img :src="require('../assets/icons/order_ap.svg')" alt="Мои заказы" class="tab-icon mr-2">
          <span>Мои заказы</span>
        </span>
        </template>
        <b-card-text>Заказы</b-card-text>
      </b-tab>

      <b-tab class="account-page_tabs__tab">
        <template #title>
          <span class="d-flex align-items-center">
            <img :src="require('../assets/icons/account_ap.svg')" alt="Учетная запись" class="tab-icon mr-2">
            <span>Учетная запись</span>
          </span>
        </template>
        <b-card-text>Данные учетной записи</b-card-text>
      </b-tab>

      <b-tab class="account-page_tabs__tab">
        <template #title>
          <span class="d-flex align-items-center">
            <img :src="require('../assets/icons/cart_ap.svg')" alt="Корзина" class="tab-icon mr-2">
            <span>Корзина</span>
          </span>
        </template>
        <b-card-text>Содержимое корзины</b-card-text>
      </b-tab>

    </b-tabs>

    <div class="account-page_exit">
      <img :src="require('../assets/icons/exit_ap.svg')" alt="Выход">
      <p>Выйти</p>
    </div>

  </div>
</template>

<script>
export default {
  name: "AccountPage"
}
</script>

<style scoped>

</style>