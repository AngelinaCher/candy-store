<template>
  <div class="main-page_new_products">

    <h1>Новинки</h1>

    <div class="main-page_new_products_block">
      <div
          class="main-page_new_product"
          v-for="product in testData"
          :key="product.id"
      >
        <img :src="require(`../../assets/icons/${product.img}`)">
        <h2> {{ product["name"] }} </h2>
        <p>{{ product["cost"] }} ₽</p>
        <b-button class="custom-button">В корзину</b-button>
      </div>

    </div>
  </div>
</template>

<script>
export default {
  name: "NewProducts",
  data() {
    return {
      testData: [
        {"id": 1, "name": "Белый шоколад Villars с ванилью", "cost": 1280, "img": "test_img.png"},
        {"id": 2, "name": "Белый шоколад Villars с ванилью", "cost": 1280, "img": "test_img.png"},
        {"id": 3, "name": "Белый шоколад Villars с ванилью", "cost": 1280, "img": "test_img.png"},
        {"id": 4, "name": "Белый шоколад Villars с ванилью", "cost": 1280, "img": "test_img.png"},
      ],
    }
  }
}
</script>
