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
        component: () => import("../views/CardPage.vue"),
    },
    {
        path: "/account",
        name: "AccountPage",
        component: () => import("../views/AccountPage.vue"),
    },
    {
        path: "/order/:orderId",
        name: "OrderPage",
        component: () => import("../views/OrderPage.vue"),
        props: true,
    },
    {
        path: "/catalog/:productName",
        name: "CatalogPage",
        component: () => import("../views/CatalogPage.vue"),
        props: true,
    },
    {
        path: "/login",
        name: "LoginPage",
        component: () => import("../views/LoginPage.vue"),
    },
    {
        path: "/registration",
        name: "RegistrationPage",
        component: () => import("../views/RegistrationPage.vue")
    },
    {
        path: "/product/:productSlug",
        name: "ProductPage",
        component: () => import("../views/ProductPage.vue"),
        props: true,
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router
