import { ActionContext, Module } from "vuex";
import axios from "axios";
import { Icontact } from "@/Interfaces/Contact";

const api = axios.create({
  baseURL: process.env.VUE_APP_API_BASE_URL,
});

interface ContactsState {
  contacts: Icontact[];
}

const contacts: Module<ContactsState, unknown> = {
  namespaced: true,
  state: {
    contacts: [],
  },
  mutations: {
    setContacts(state, payload: Icontact[]) {
      state.contacts = payload;
    },
  },
  actions: {
    async fetchContacts({ commit }: ActionContext<ContactsState, unknown>) {
      const { data } = await api.get("/api/v1/contacts");
      commit("setContacts", data);
    },
    async fetchContact(
      _: ActionContext<ContactsState, unknown>,
      id: number
    ): Promise<Icontact> {
      const { data } = await api.get(`/api/v1/contacts/${id}`);
      return data;
    },
    async createContact(
      _: ActionContext<ContactsState, unknown>,
      contact: Icontact
    ) {
      await api.post("/api/v1/contacts", contact);
    },
    async updateContact(
      _: ActionContext<ContactsState, unknown>,
      contact: Icontact
    ) {
      await api.put(`/api/v1/contacts/${contact.id}`, contact);
    },
    async deleteContact(
      { dispatch }: ActionContext<ContactsState, unknown>,
      id: number
    ) {
      await api.delete(`/api/v1/contacts/${id}`);
      dispatch("fetchContacts");
    },
    async fetchAddressByCep(
      _: ActionContext<ContactsState, unknown>,
      cep: string
    ) {
      const { data } = await api.get(`/api/v1/cep/${cep}`);
      return data;
    },
  },
  getters: {
    contacts: (state) => state.contacts,
  },
};

export default contacts;
