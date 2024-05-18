<template>
  <div id="app">
    <AppHeader/>
    <router-view/>
    <AppFooter/>
  </div>
</template>

<script>
import axios from "axios";

import AppHeader from "./components/app/AppHeader.vue";
import AppFooter from "./components/app/AppFooter.vue";

export default {
  name: "MainPage",
  components: {
    AppHeader,
    AppFooter,
  },
  beforeCreate() {
    this.$store.commit("initializeStore");

    const token = this.$store.state.tokenData;

    if (token["access_token"] !== "" && token["refresh_token"] !== "") {
      axios.defaults.headers.common['Authorization'] = `Bearer ${token['access_token']}`;
    } else {
      axios.defaults.headers.common['Authorization'] = "";
    }
  },
}
</script>

<style lang="scss">
@import "./assets/styles/main.scss";
</style>
