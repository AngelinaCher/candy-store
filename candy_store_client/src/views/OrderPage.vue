<template>
  <div class="order-page">
    <div class="cart-page_header">
      <h1>Заказ № {{this.orderId}}</h1>
    </div>
  </div>
</template>

<script>
export default {
  name: "OrderPage",
  props: ["orderId"],
  data() {
    return {
      order: {},
    }
  },
}
</script>