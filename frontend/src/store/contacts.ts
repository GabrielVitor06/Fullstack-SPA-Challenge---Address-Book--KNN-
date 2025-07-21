import { Module } from "vuex";
import axios from "axios";
import { Icontact } from "@/Interfaces/Contact";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000/contacts",
});

interface State {
  contacts: Icontact[];
}

const contacts: Module<State, unknown> = {
  namespaced: true,
  state: {
    contacts: [],
  },
  mutations: {
    setContacts(state, payload) {
      state.contacts = payload;
    },
  },
  actions: {
    async fetchContacts({ commit }) {
      const { data } = await api.get("/contacts");
      commit("setContacts", data);
    },
    async fetchContact(_, id: number) {
      const { data } = await api.get(`/contacts/${id}`);
      return data;
    },
    async createContact(_, contact: Icontact) {
      await api.post("/contacts", contact);
    },
    async updateContact(_, contact: Icontact) {
      await api.put(`/contacts/${contact.id}`, contact);
    },
    async deleteContact({ dispatch }, id: number) {
      await api.delete(`/contacts/${id}`);
      dispatch("fetchContacts");
    },
  },
  getters: {
    contacts: (state) => state.contacts,
  },
};

export default contacts;
