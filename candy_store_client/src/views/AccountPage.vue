<template>
  <div class="account-page">

    <div class="cart-page_header">
      <h1>Личный кабинет</h1>
    </div>

    <b-tabs pills card vertical class="account-page_tabs">

      <b-tab active class="account-page_tabs__tab">
        <template #title>
        <span class="d-flex align-items-center">
          <img
              :src="require('../assets/icons/order_ap.svg')"
              alt="Мои заказы"
              class="tab-icon mr-2"
          >
          <span>Мои заказы</span>
        </span>
        </template>
        <b-card-text>
          <Orders
              :orders="orderData"
          />
        </b-card-text>
      </b-tab>

      <b-tab class="account-page_tabs__tab">
        <template #title>
          <span class="d-flex align-items-center">
            <img
                :src="require('../assets/icons/account_ap.svg')"
                alt="Учетная запись"
                class="tab-icon mr-2"
            >
            <span>Учетная запись</span>
          </span>
        </template>
        <b-card-text>
          <Account
              :userData="userData"
              @changePassword="changePassword"
          />
        </b-card-text>
      </b-tab>

      <b-tab class="account-page_tabs__tab">
        <template #title>
          <router-link
              to="/cart" class="d-flex align-items-center"
              style="text-decoration: none; color: #000000;"
          >
            <img
                :src="require('../assets/icons/cart_ap.svg')"
                alt="Корзина"
                class="tab-icon mr-2"
            >
            <span>Корзина</span>
          </router-link>
        </template>
      </b-tab>

    </b-tabs>

    <div class="account-page_exit">
      <img :src="require('../assets/icons/exit_ap.svg')" alt="Выход">
      <p>Выйти</p>
    </div>

  </div>
</template>

<script>
import axios from "axios";

import Orders from "../components/account-page/Orders.vue";
import Account from "../components/account-page/Account.vue";

export default {
  name: "AccountPage",
  components: {
    Orders,
    Account,
  },
  mounted() {
    document.title = "Аккаунт | Карамелька ";
    this.getUserData();
    this.getOrdersData();
  },
  data() {
    return {
      userData: {
        "name": "",
        "second_name": "",
        "email": "",
        "password": "",
      },
      orderData: [],
    }
  },
  methods: {
    changePassword(password) {
      console.log(password);
    },
    async getUserData() {
      await axios
          .get("http://127.0.0.1:8000/api/v1/profile/")
          .then(response => {
            this.userData["name"] = response["data"]["firstname"];
            this.userData["second_name"] = response["data"]["lastname"];
            this.userData["email"] = response["data"]["email"];
            this.userData["password"] = "*************";
          })
          .catch(err => console.log(err))
    },
    async getOrdersData() {
      await axios
          .get("http://127.0.0.1:8000/api/v1/user-orders/")
          .then(response => {
            this.orderData = response.data;
          })
          .catch(err => console.log(err))
    },
  }
}
</script>