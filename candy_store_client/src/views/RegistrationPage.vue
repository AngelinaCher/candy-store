<template>
  <div class="registration-page">
    <div class="cart-page_header">
      <h1>Регистрация</h1>
    </div>

    <div class="login-page_field">
      <label for="range-2">Логин</label>
      <b-form-input
          placeholder="Введите логин"
          class="custom-input login-page_field__input"
      ></b-form-input>
    </div>

    <div class="login-page_field">
      <label for="range-2">E-mail</label>
      <b-form-input
          placeholder="Введите логин"
          class="custom-input login-page_field__input"
      ></b-form-input>
    </div>

    <div class="login-page_field">
      <label for="range-2">Пароль</label>
      <b-form-input
          placeholder="Введите пароль"
          class="custom-input login-page_field__input"
          type="password"
      ></b-form-input>
    </div>

    <div class="login-page_field">
      <label for="range-2">Пароль</label>
      <b-form-input
          placeholder="Повторите пароль"
          class="custom-input login-page_field__input"
          type="password"
      ></b-form-input>
    </div>

    <div class="login-page_btn">
      <b-button
          class="custom-button"
          @click="register"
      >Зарегистрироваться
      </b-button>
    </div>

    <div class="login-page_link">Уже есть аккаунт?
      <router-link to="/login">Вход</router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: "RegistrationPage",
  mounted() {
    document.title = "Регистрация | Карамелька "
  },
}
</script>

<style scoped>

</style>