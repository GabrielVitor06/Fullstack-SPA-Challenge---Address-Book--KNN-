import { ActionContext, Module } from "vuex";
import axios from "axios";
import { Icontact } from "@/Interfaces/Contact";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000/api/v1",
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
      const { data } = await api.get("/contacts");
      commit("setContacts", data);
    },
    async fetchContact(
      _: ActionContext<ContactsState, unknown>,
      id: number
    ): Promise<Icontact> {
      const { data } = await api.get(`/contacts/${id}`);
      return data;
    },
    async createContact(
      _: ActionContext<ContactsState, unknown>,
      contact: Icontact
    ) {
      await api.post("/contacts", contact);
    },
    async updateContact(
      _: ActionContext<ContactsState, unknown>,
      contact: Icontact
    ) {
      await api.put(`/contacts/${contact.id}`, contact);
    },
    async deleteContact(
      { dispatch }: ActionContext<ContactsState, unknown>,
      id: number
    ) {
      await api.delete(`/contacts/${id}`);
      dispatch("fetchContacts");
    },
    async fetchAddressByCep(
      _: ActionContext<ContactsState, unknown>,
      cep: string
    ) {
      const { data } = await api.get(`/cep/${cep}`);
      return data;
    },
  },
  getters: {
    contacts: (state) => state.contacts,
  },
};

export default contacts;
