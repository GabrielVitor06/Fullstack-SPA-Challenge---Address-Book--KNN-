import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import vuetify from "./plugins/vuetify";
import axios from "axios";
import { library } from "@fortawesome/fontawesome-svg-core";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { faUserSlash } from "@fortawesome/free-solid-svg-icons";

library.add(faUserSlash);

Vue.component("font-awesome-icon", FontAwesomeIcon);

Vue.config.productionTip = false;

axios.defaults.baseURL = "http://localhost:8000";

new Vue({
  router,
  store,
  vuetify,
  render: (h) => h(App),
}).$mount("#app");
