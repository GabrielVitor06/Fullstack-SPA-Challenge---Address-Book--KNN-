<template>
  <v-bottom-sheet v-model="isDialogOpen" persistent>
    <v-card>
      <v-card-title>
        <span class="text-h6">{{
          contactId ? "Editar Contato" : "Novo Contato"
        }}</span>
      </v-card-title>

      <v-card-text>
        <v-form ref="formRef" @submit.prevent="handleSubmit">
          <v-text-field
            v-model="contact.name"
            label="Nome"
            :rules="[required]"
            required
          />
          <v-text-field
            v-model="contact.email"
            label="Email"
            :rules="[required, emailRule]"
            required
          />
          <v-text-field
            v-model="contact.phone"
            label="Telefone"
            :rules="[required]"
            required
            v-mask="'(##) #####-####'"
          />
          <v-text-field
            v-model="contact.cep"
            label="CEP"
            maxlength="9"
            @blur="fetchAddress"
            :rules="[required]"
            required
            v-mask="'#####-###'"
          />

          <v-text-field
            v-model="contact.address.logradouro"
            label="Logradouro"
            disabled
          />
          <v-text-field
            v-model="contact.address.bairro"
            label="Bairro"
            disabled
          />
          <v-text-field
            v-model="contact.address.cidade"
            label="Cidade"
            disabled
          />
          <v-text-field
            v-model="contact.address.estado"
            label="Estado"
            disabled
          />
        </v-form>
      </v-card-text>

      <v-card-actions>
        <v-spacer />
        <v-btn text @click="close">Cancelar</v-btn>
        <v-btn color="primary" @click="handleSubmit">Salvar</v-btn>
      </v-card-actions>
    </v-card>
  </v-bottom-sheet>
</template>

<script lang="ts">
import Vue from "vue";
import { Icontact } from "@/Interfaces/Contact";
import axios from "axios";
import {
  createEmptyContact,
  formatContact,
  formatAddress,
} from "@/utils/contact";

export default Vue.extend({
  props: {
    contactId: {
      type: [String, Number],
      required: false,
    },
    value: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      isDialogOpen: this.value,
      contact: createEmptyContact() as Icontact,
      required: (v: string) => !!v || "Campo obrigatório",
      emailRule: (v: string) => /.+@.+\..+/.test(v) || "E-mail inválido",
    };
  },
  watch: {
    contactId(newId) {
      if (this.isDialogOpen) {
        if (newId) {
          this.fetchContact();
        } else {
          this.resetForm();
        }
      }
    },
    value(val: boolean) {
      this.isDialogOpen = val;
      if (val) {
        if (this.contactId) {
          this.fetchContact();
        } else {
          this.resetForm();
        }
      }
    },
    isDialogOpen(val: boolean) {
      this.$emit("input", val);
    },
  },
  methods: {
    resetForm() {
      this.contact = createEmptyContact();
    },
    close() {
      this.isDialogOpen = false;
    },
    async fetchContact() {
      if (!this.contactId) return;
      try {
        const data = await this.$store.dispatch(
          "contacts/fetchContact",
          Number(this.contactId)
        );
        this.contact = formatContact(data);
      } catch (error) {
        console.error(error);
        this.$emit("show-snackbar", {
          message: "Erro ao buscar contato",
          color: "error",
        });
      }
    },

    async fetchAddress() {
      if (this.contact.cep?.length === 8) {
        try {
          const { data } = await axios.get(
            `http://127.0.0.1:8000/contacts/cep/${this.contact.cep}`
          );
          this.contact.address = formatAddress(data, this.contact.cep);
        } catch {
          this.$emit("show-snackbar", {
            message: "CEP inválido!",
            color: "error",
          });
        }
      }
    },

    async handleSubmit() {
      const valid = await (this.$refs.formRef as any).validate();
      if (!valid) return;

      try {
        if (this.contactId) {
          await this.$store.dispatch("contacts/updateContact", this.contact);
        } else {
          console.log("Criando contato:", this.contact);
          await this.$store.dispatch("contacts/createContact", this.contact);
        }
        this.$emit("saved");
        this.isDialogOpen = false;
      } catch (error) {
        this.$emit("show-snackbar", {
          message: "Erro ao salvar contato.",
          color: "error",
        });
      }
    },
  },
});
</script>
