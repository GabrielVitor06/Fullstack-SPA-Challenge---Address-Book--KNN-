<template>
  <v-form @submit.prevent="handleSubmit" ref="formRef">
    <v-text-field v-model="contact.name" label="Nome" required />
    <v-text-field v-model="contact.email" label="Email" required />
    <v-text-field v-model="contact.phone" label="Telefone" required />
    <v-text-field
      v-model="contact.cep"
      label="CEP"
      @blur="fetchAddress"
      required
      maxlength="8"
    />

    <v-text-field
      v-model="contact.address.logradouro"
      label="Logradouro"
      disabled
    />
    <v-text-field v-model="contact.address.bairro" label="Bairro" disabled />
    <v-text-field v-model="contact.address.cidade" label="Cidade" disabled />
    <v-text-field v-model="contact.address.estado" label="Estado" disabled />

    <v-row justify="space-between" class="mt-4">
      <v-btn text @click="$emit('cancel')">Cancelar</v-btn>
      <v-btn color="primary" type="submit">Salvar</v-btn>
    </v-row>
  </v-form>
</template>

<script lang="ts">
import Vue from "vue";
import axios from "axios";
import { contact } from "@/Interfaces/Contact";

export default Vue.extend({
  props: {
    contactId: {
      type: String,
      required: false,
    },
  },
  data() {
    return {
      contact: {
        name: "",
        email: "",
        phone: "",
        cep: "",
        address: {
          logradouro: "",
          bairro: "",
          cidade: "",
          estado: "",
          cep: "",
        },
      } as contact,
    };
  },
  async created() {
    if (this.contactId) {
      await this.fetchContact();
    }
  },
  methods: {
    async fetchContact() {
      try {
        const { data } = await axios.get(`/contacts/${this.contactId}`);
        this.contact = {
          ...data,
          address: data.address ?? {
            logradouro: "",
            bairro: "",
            cidade: "",
            estado: "",
            cep: "",
          },
        };
      } catch {
        alert("Erro ao buscar contato");
      }
    },
    async fetchAddress() {
      if (this.contact.cep?.length === 8) {
        try {
          const { data } = await axios.get(`/cep/${this.contact.cep}`);
          this.contact.address = {
            logradouro: data.logradouro,
            bairro: data.bairro,
            cidade: data.cidade,
            estado: data.estado,
            cep: this.contact.cep,
          };
        } catch {
          alert("CEP inválido!");
        }
      }
    },
    async handleSubmit() {
      try {
        if (this.contactId) {
          await axios.put(`/contacts/${this.contactId}`, this.contact);
        } else {
          await axios.post("/contacts", this.contact);
        }
        this.$emit("saved", this.contact);
      } catch {
        alert("Erro ao salvar contato.");
      }
    },
  },
});
</script>
