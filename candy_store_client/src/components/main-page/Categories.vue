<template>
  <div class="main-page_categories">
    <router-link
        class="main-page_categories_category"
        v-for="cat in testData"
        :key="cat.id" to="/"
    >
      <h1>{{ cat["category"] }}</h1>
      <p>{{ cat["desc"] }}</p>
      <!--      <img :src="require(`${cat.img}`)" alt="">-->
    </router-link>
  </div>
</template>

<script>
export default {
  name: "Categories",
  data() {
    return {
      testData: [
        {"id": 1, "category": "Батончики", "desc": "Питательные для активного образа жизни", "img": "",},
        {"id": 2, "category": "Шоколад", "desc": "Нежные и ароматные, для сладкого утешения", "img": "",},
        {"id": 3, "category": "Печенье", "desc": "Хрустящие и нежные для домашнего уюта", "img": "",},
        {"id": 4, "category": "Мармелад", "desc": "Сладкие, сочные, для радости и удовольствия", "img": "",},
        {"id": 5, "category": "Сладкие подарки", "desc": "Радостные комплекты, для особых моментов", "img": "",},
        {"id": 6, "category": "Конфеты", "desc": "Роскошные, изысканные, для настоящих гурманов", "img": "",}
      ]
    }
  }
}
</script>

