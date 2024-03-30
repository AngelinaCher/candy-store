<template>
  <div class="cart-page">
    <div class="cart-page_header">
      <h1>Корзина</h1>
      <p> 0 товаров</p>
      <span class="cart-page_header__btn">Очистить корзину</span>
    </div>

    <div class="cart-page_content">

      <div
          class="cart-page_content__items"
      >
        <div
            class="cart-page_content__items_item"
            v-for="item in testData"
            :key="item.id"
        >

          <div class="cart-page_content__items_img">
            <img :src="require(`../assets/icons/${item.img}`)">
          </div>

          <div class="cart-page_content__items_info">
            <h2> {{ item["name"] }} </h2>
            <p> {{ item["cost"] }} ₽</p>
          </div>

          <div class="cart-page_content__items_amount">

            <div class="cart-page_content__items_amount__sign">
              <img src="../assets/icons/minus.svg" alt="minus">
            </div>

            <div class="cart-page_content__items_amount__amount">{{ item["amount"] }}</div>

            <div class="cart-page_content__items_amount__sign">
              <img src="../assets/icons/plus.svg" alt="plus">
            </div>

          </div>
        </div>
      </div>

      <div class="cart-page_content__result">

        <div class="cart-page_header__all">
          <div class="cart-page_header__all_count">3 товара</div>
          <div class="cart-page_header__all_price">48 000 ₽</div>
        </div>

        <div class="cart-page_header__discount">
          <div class="cart-page_header__all_count">Скидка</div>
          <div class="cart-page_header__all_price">-16 000 ₽</div>
        </div>

        <hr>

        <div class="cart-page_header__discount">
          <div class="cart-page_header__all_count result">Итого:</div>
          <div class="cart-page_header__all_price result">32 000 ₽</div>
        </div>

        <b-button
            class="cart-page_header__discount_btn custom-button"
        >Оформить заказ
        </b-button>

      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "CardPage",
  mounted() {
    document.title = "Корзина | Карамелька "
  },
  data() {
    return {
      testData: [
        {"id": 1, "name": "Белый шоколад Villars с ванилью", "cost": 404, "amount": 2, "img": "test_img.png",},
        {"id": 2, "name": "Белый шоколад Villars с ванилью", "cost": 404, "amount": 1, "img": "test_img.png",}
      ]
    }
  }
}
</script>