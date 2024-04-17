<template>
  <div class="main-page_banner">

    <h1>Скидка дня на все</h1>

    <p>
      Получите 15% скидку на весь ассортимент сладостей при оформлении заказа сегодня.
      <br> Успейте насладиться вкусом по выгодной цене!
    </p>

    <router-link :to="{ name: 'CatalogPage', params: { productName: '8/batonchiki' }}">
      <b-button
          class="main-page_banner__btn custom-button"
      >Перейти к покупкам
      </b-button>
    </router-link>
  </div>
</template>

<script>
export default {
  name: "Banner",
}
</script>