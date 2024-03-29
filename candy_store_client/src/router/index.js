import Vue from "vue";
import VueRouter from "vue-router";

Vue.use(VueRouter)

const routes = [
    {
        path: "/",
        name: "MainPage",
        component: () => import("../views/MainPage.vue"),
    },
    {
        path: "/cart",
        name: "CartPage",
        component: () => import("../views/CardPage.vue")
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router
