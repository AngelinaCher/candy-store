<template>
  <div class="catalog-page">

    <div class="cart-page_header">
      <h1>{{ productName }}</h1>
    </div>
  </div>
</template>

<script>
export default {
  name: "CatalogPage",
  props: ["productName"],
  mounted() {
    document.title = "Каталог | Карамелька "
  },
}
</script>