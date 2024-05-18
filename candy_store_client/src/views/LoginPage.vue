<template>
  <div class="login-page">
    <div class="cart-page_header">
      <h1>Вход</h1>
    </div>

    <div class="login-page_field">
      <label for="range-2">E-mail</label>
      <b-form-input
          placeholder="Введите e-mail"
          class="custom-input login-page_field__input"
          v-model="email"
      ></b-form-input>
    </div>

    <div class="login-page_field">
      <label for="range-2">Пароль</label>
      <b-form-input
          placeholder="Введите пароль"
          class="custom-input login-page_field__input"
          type="password"
          v-model="password"
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
import axios from "axios";

export default {
  name: "LoginPage",
  mounted() {
    document.title = "Вход | Карамелька "
  },
  data() {
    return {
      email: "",
      password: ""
    }
  },
  methods: {
    async login() {
      const userData = {
        "email": this.email,
        "password": this.password,
      };
      await axios
          .post("http://127.0.0.1:8000/api/v1/auth/login/", userData)
          .then(response => {
            if (response.data["access"] !== "" && response.data["refresh"] !== "") {
              this.$store.commit("setToken", response.data);

              axios.defaults.headers.common["Authorization"] = `Bearer ${response.data['access']}`;

              localStorage.setItem("access_token", response.data["access"]);
              localStorage.setItem("refresh_token", response.data["refresh"]);

              const toPath = "/account";
              this.$router.push(toPath);
            } else {
              console.log("Что-то пошло не так")
            }
          })
          .catch(err => console.log(err))
    },
  }
}
</script>