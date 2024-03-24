<template>
  <div id="app">
    <AppHeader />
    <router-view/>
  </div>
</template>

<script>
import AppHeader from "./components/app/AppHeader.vue";

export default {
  name: "MainPage",
  components: {
    AppHeader,
  }
}
</script>

<style lang="scss">
@import "./assets/styles/main.scss";
</style>
