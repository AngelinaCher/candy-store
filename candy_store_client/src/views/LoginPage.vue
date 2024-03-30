<template>
  <div class="login-page">
    <div class="cart-page_header">
      <h1>Вход</h1>
    </div>

    <div class="login-page_field">
      <label for="range-2">Логин</label>
      <b-form-input
          v-model="userData.username"
          placeholder="Введите логин"
          class="custom-input login-page_field__input"
      ></b-form-input>
    </div>

    <div class="login-page_field">
      <label for="range-2">Пароль</label>
      <b-form-input
          v-model="userData.password"
          placeholder="Введите пароль"
          class="custom-input login-page_field__input"
          type="password"
      ></b-form-input>
    </div>

    <div class="login-page_btn">
      <b-button
          class="custom-button"
          @click="login"
      >Войти
      </b-button>
    </div>

    <div class="login-page_link">Еще не зарегистрированы?
      <router-link to="/registration">Регистрация</router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: "LoginPage",
  mounted() {
    document.title = "Вход | Карамелька "
  },
  data() {
    return {
      userData: {
        "username": "",
        "password": "",
      }
    }
  }
}
</script>