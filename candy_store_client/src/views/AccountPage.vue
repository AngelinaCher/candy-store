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
import Orders from "../components/account-page/Orders.vue";
import Account from "../components/account-page/Account.vue";

export default {
  name: "AccountPage",
  components: {
    Orders,
    Account,
  },
  mounted() {
    document.title = "Аккаунт | Карамелька "
  },
  data() {
    return {
      userData: {
        "name": "Иван",
        "second_name": "Иванов",
        "email": "ivanov@mail.ru",
        "password": "test",
      },
      orderData: [
        {
          "date": "12.01.2024",
          "number_order": "445567-879234",
          "amount": "12 000",
        },
        {
          "date": "01.02.24",
          "number_order": "445567-879233",
          "amount": "23 000",
        }
      ],
    }
  },
  methods: {
    changePassword(password) {
      console.log(password);
    }
  }
}
</script>