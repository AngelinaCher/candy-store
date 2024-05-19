<template>
  <div class="account-page_orders">

    <router-link
        class="account-page_order"
        v-for="order in orders"
        :key="order['order_id']" :to="{ name: 'OrderPage', params: { orderId: order['order_id'] }}"
    >
      <h1> Заказ от {{ order["required_date"] }} </h1>
      <p> {{ order['payment_method'] }} </p>
      <span> {{ order['total_price'] }} ₽ </span>
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