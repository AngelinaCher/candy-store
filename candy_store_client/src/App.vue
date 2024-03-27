<template>
  <div id="app">
    <AppHeader/>
    <router-view/>
    <AppFooter />
  </div>
</template>

<script>
import AppHeader from "./components/app/AppHeader.vue";
import AppFooter from "./components/app/AppFooter.vue";

export default {
  name: "MainPage",
  components: {
    AppHeader,
    AppFooter,
  },
}
</script>

<style lang="scss">
@import "./assets/styles/main.scss";
</style>
