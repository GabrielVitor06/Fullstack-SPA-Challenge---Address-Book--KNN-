import Vue from "vue";
import Router from "vue-router";
import ContactList from "@/views/ContactList.vue";
import ContactFormPage from "@/views/ContactFormPage.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    { path: "/contacts", component: ContactList },
    { path: "/contacts/new", component: ContactFormPage },
    { path: "/contacts/:id/edit", component: ContactFormPage, props: true },
    { path: "*", redirect: "/contacts" },
  ],
});
