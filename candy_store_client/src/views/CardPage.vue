<template>
  <div class="cart-page">
    <div class="cart-page_header">
      <h1>Корзина</h1>
      <p> {{ total_quantity }} товаров</p>
      <span class="cart-page_header__btn">Очистить корзину</span>
    </div>

    <div class="cart-page_content">

      <div
          class="cart-page_content__items"
      >
        <div
            class="cart-page_content__items_item"
            v-for="item in cart"
            :key="item.product_id"
        >

          <div class="cart-page_content__items_img">
            <img :src="item.image" style="width: 300px; height: 250px;">
          </div>

          <div class="cart-page_content__items_info">
            <h2> {{ item["product_name"] }} </h2>
            <p> {{ item["price"] }} ₽</p>
          </div>

          <div class="cart-page_content__items_amount">

            <div class="cart-page_content__items_amount__sign">
              <img src="../assets/icons/minus.svg" alt="minus" @click="decreaseAmount">
            </div>

            <div class="cart-page_content__items_amount__amount">{{ item["product_quantity"] }}</div>

            <div class="cart-page_content__items_amount__sign">
              <img src="../assets/icons/plus.svg" alt="plus" @click="increaseAmount">
            </div>

          </div>
        </div>
      </div>

      <div class="cart-page_content__result">

        <div class="cart-page_header__all">
          <div class="cart-page_header__all_count">{{ total_quantity }} товаров</div>
          <div class="cart-page_header__all_price">{{ total_price }} ₽</div>
        </div>

        <!--        <div class="cart-page_header__discount">-->
        <!--          <div class="cart-page_header__all_count">Скидка</div>-->
        <!--          <div class="cart-page_header__all_price">-16 000 ₽</div>-->
        <!--        </div>-->

        <hr>

        <div class="cart-page_header__discount">
          <div class="cart-page_header__all_count result">Итого:</div>
          <div class="cart-page_header__all_price result">{{ total_price }} ₽</div>
        </div>

        <b-button
            class="cart-page_header__discount_btn custom-button"
            @click="createOrder"
        >Оформить заказ
        </b-button>

      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "CardPage",
  mounted() {
    document.title = "Корзина | Карамелька ";
    this.getCard();
  },
  data() {
    return {
      cart: [],
      total_price: 0,
      total_quantity: 0,
      cart_id: "",
    }
  },
  methods: {
    async getCard() {
      await axios
          .get("http://127.0.0.1:8000/api/v1/cart")
          .then(response => {
            this.cart = response.data["cart_items"];
            this.total_price = response.data["total_price"];
            this.total_quantity = response.data["total_quantity"];
            this.cart_id = response.data["cart_id"];
            console.log(response.data)
          })
    },
    increaseAmount() {
      console.log("add");
    },
    decreaseAmount() {
      console.log("del");
    },
    async createOrder() {
      const currentDate = new Date();
      const day = String(currentDate.getDate()).padStart(2, '0');
      const month = String(currentDate.getMonth() + 1).padStart(2, '0');
      const year = currentDate.getFullYear();
      const formattedDate = `${day}.${month}.${year}`;

      await axios
          .post(
            "http://127.0.0.1:8000/api/v1/order/create/",
            {
              "cart_id": this.cart_id,
              "required_date": formattedDate,
              "payment_method": "Наличные"
            }
          )
          .then(response => {
            if (response.status === 201) {
              const toPath = "/account";
              this.$router.push(toPath);
            }
          })
          .catch(err => console.log(err))
    }
  }
}
</script>