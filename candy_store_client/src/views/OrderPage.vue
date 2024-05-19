<template>
  <div class="order-page">

    <div class="cart-page_header">
      <h1>Заказ № {{ this.orderId }}</h1>
    </div>

    <b-table
                striped
                hover
                :items="order['cart_items']"
                :fields="fields"
                
    ></b-table>

    <b-card
        border-variant="warning"
        header-bg-variant="transparent"
        align="center"
      >
        <b-card-text style="font-size: 20px;">Всего товаров: {{ totalQuantity }}</b-card-text>
        <b-card-text style="font-size: 20px;">Итоговая стоимость: {{ totalPrice }}</b-card-text>
        <b-card-text style="font-size: 20px;">Статус заказа: {{ status }}</b-card-text>

        <b-button
          class="cart-page_header__discount_btn custom-button"
          @click="createOrder"
        >Повторить заказ
        </b-button>
    </b-card>

  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "OrderPage",
  props: ["orderId"],
  mounted() {
    document.title = "Заказ | Карамелька ";
    this.getOrderDetails();
  },
  data() {
    return {
      order: {},
      fields: [
        {key: "product_name", label: "Название товара",},
        {key: "price", label: "Цена",},
        {key: "unit", label: "Единица измерения",},
        {key: "product_quantity", label: "Количество",},
        {key: "price", label: "Цена",}
      ],
      totalPrice: 0,
      totalQuantity: 0,
      status: "",
    }
  },
  methods: {
    async getOrderDetails() {
      await axios
          .get(`http://127.0.0.1:8000/api/v1/order/?order_id=${this.orderId}`)
          .then(response => {
            console.log(response.data)
            this.order = response.data;
            this.totalPrice = response.data["total_price"];
            this.totalQuantity = response.data["total_quantity"];
            this.status = response.data["status"];
          })
          .catch(err => console.log(err))
    },
    createOrder() {

    },
  }
}
</script>