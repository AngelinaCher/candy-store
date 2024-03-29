<template>
  <div class="account-page_account">

    <div class="account-page_account__data">

      <div class="account-page_account__data_el">
        <div>
          <label for="range-2">Имя</label>
          <b-form-input
              v-model="localUserData.name"
              placeholder="Имя"
              class="custom-input"
          ></b-form-input>
        </div>

        <div>
          <label for="range-2">Фамилия</label>
          <b-form-input
              v-model="localUserData['second_name']"
              placeholder="Фамилия"
              class="custom-input"
          ></b-form-input>
        </div>
      </div>

      <br>

      <div class="account-page_account__data_el">
        <div>
          <label for="range-2">Почта</label>
          <b-form-input
              v-model="localUserData['email']"
              placeholder="Почта"
              type="email"
              class="custom-input"
          ></b-form-input>
        </div>
        <div>
          <label for="range-2">Пароль</label>
          <b-form-input
              v-model="localUserData['password']"
              placeholder="Пароль"
              type="password"
              class="custom-input"
          ></b-form-input>
        </div>
      </div>

    </div>

    <div class="account-page_account__btn">
      <b-button
          class="custom-button"
          @click="changePassword"
      >Изменить пароль
      </b-button>
    </div>
  </div>


</template>

<script>
export default {
  name: "Account",
  props: {
    userData: {
      required: true,
      type: Object,
    }
  },
  data() {
    return {
      localUserData: this.userData,
    }
  },
  methods: {
    changePassword() {
      this.$emit("changePassword", this.localUserData["password"]);
    }
  }
}
</script>