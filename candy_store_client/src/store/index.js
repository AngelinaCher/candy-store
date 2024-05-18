import Vue from "vue";
import Vuex from "vuex";

import axios from 'axios';

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        tokenData: {
            "access_token": "",
            "refresh_token": "",
            "type_token": "Bearer",
        },
        isAuthenticated: false,
    },
    getters: {},
    mutations: {
        setToken(state, tokenData) {
            state.tokenData["access_token"] = tokenData["access"];
            state.tokenData["refresh_token"] = tokenData["refresh"];
            state.isAuthenticated = true;
        },
        async initializeStore(state) {
            if (localStorage.getItem('access_token') && localStorage.getItem('refresh_token')) {
                await axios
                    .post("http://127.0.0.1:8000/api/v1/auth/jwt/verify/", {token: localStorage.getItem("access_token")})
                    .then(response => {
                        state.tokenData['access_token'] = localStorage.getItem('access_token');
                        state.tokenData['refresh_token'] = localStorage.getItem('refresh_token');
                        axios.defaults.headers.common["Authorization"] = `Bearer ${state.tokenData['access_token']}`;
                        state.isAuthenticated = true;
                    })
                    .catch(err => {
                        if (err["message"] === "Request failed with status code 401") {
                            axios.post(
                                "http://127.0.0.1:8000/api/v1/auth/jwt/refresh/",
                                {"refresh": localStorage.getItem('refresh_token')}
                            )
                                .then(response => {
                                    if (response.data["access"]) {
                                        axios.defaults.headers.common["Authorization"] = `Bearer ${response.data["access"]}`;
                                        localStorage.setItem("access_token", response.data["access"]);
                                        state.tokenData["access_token"] = response.data["access"];
                                        state.isAuthenticated = true;
                                    } else {
                                        localStorage.removeItem("access_token");
                                        localStorage.removeItem("refresh_token");
                                        state.tokenData["access_token"] = "";
                                        state.tokenData["refresh_token"] = "";
                                        state.isAuthenticated = false;
                                        axios.defaults.headers.common["Authorization"] = "";
                                    }
                                })
                        }
                    })
            } else {
                localStorage.removeItem("access_token");
                localStorage.removeItem("refresh_token");
                state.tokenData["access_token"] = "";
                state.tokenData["refresh_token"] = "";
                state.isAuthenticated = false;
            }
        },
    },
    actions: {},
    modules: {}
})
