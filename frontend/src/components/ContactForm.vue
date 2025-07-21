<template>
  <v-container>
    <v-card>
      <v-card-title>
        <span class="text-h6">
          {{ contactId ? "Editar Contato" : "Novo Contato" }}
        </span>
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
        <v-btn text @click="goBack">Cancelar</v-btn>
        <v-btn color="primary" @click="handleSubmit">Salvar</v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script lang="ts">
import Vue from "vue";
import { createEmptyContact, formatContact } from "@/utils/contact";

export default Vue.extend({
  name: "ContactForm",
  props: {
    contactId: {
      type: [String, Number],
      default: null,
    },
  },
  data() {
    return {
      contact: createEmptyContact(),
      required: (v: string) => !!v || "Campo obrigatório",
      emailRule: (v: string) => /.+@.+\..+/.test(v) || "E-mail inválido",
    };
  },
  watch: {
    contactId: {
      immediate: true,
      handler(newId) {
        if (newId) {
          this.fetchContact();
        } else {
          this.resetForm();
        }
      },
    },
  },
  methods: {
    resetForm() {
      this.contact = createEmptyContact();
    },
    goBack() {
      this.$router.push("/contacts");
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
        this.triggerSnackbar("Erro ao buscar contato", "error");
      }
    },
    async fetchAddress() {
      const rawCep = this.contact.cep?.replace(/\D/g, "");
      if (rawCep?.length === 8) {
        try {
          const data = await this.$store.dispatch(
            "contacts/fetchAddressByCep",
            rawCep
          );
          this.contact.address = {
            ...this.contact.address,
            ...data,
            cep: this.contact.cep,
          };
        } catch {
          this.triggerSnackbar("CEP inválido!", "error");
        }
      }
    },
    async handleSubmit() {
      const valid = await (
        this.$refs.formRef as unknown as {
          validate: () => boolean | Promise<boolean>;
        }
      )?.validate?.();
      if (!valid) return;

      try {
        if (this.contactId) {
          await this.$store.dispatch("contacts/updateContact", this.contact);
        } else {
          await this.$store.dispatch("contacts/createContact", this.contact);
        }
        this.goBack();
        this.triggerSnackbar("Contato salvo com sucesso!", "success");
      } catch (error) {
        this.triggerSnackbar("Erro ao salvar contato.", "error");
      }
    },
    triggerSnackbar(message: string, color: "success" | "error") {
      this.$store.dispatch("snackbar/triggerSnackbar", { message, color });
    },
  },
});
</script>
