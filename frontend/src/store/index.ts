import Vue from "vue";
import Vuex from "vuex";
import contacts from "./contacts";
import snackbar from "./snackbar";

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    contacts,
    snackbar,
  },
});
