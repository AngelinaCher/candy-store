<template>
  <div class="account-page_orders">

    <router-link
        class="account-page_order"
        v-for="order in orders"
        :key="order['number_order']" :to="{ name: 'OrderPage', params: { orderId: order['number_order'] }}"
    >
      <h1> Заказ от {{ order["date"] }} </h1>
      <p> {{ order['number_order'] }} </p>
      <span> {{ order['amount'] }} ₽ </span>
    </router-link>
  </div>
</template>

<script>
export default {
  name: "Orders",
  props: {
    orders: {
      type: Array, Object,
    }
  }
}
</script>