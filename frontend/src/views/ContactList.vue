<template>
  <v-container>
    <v-row justify="space-between" align="center" style="gap: 2rem">
      <h1>Contatos</h1>
      <v-text-field
        v-model="search"
        label="Buscar por nome"
        prepend-inner-icon="mdi-magnify"
        clearable
      />
      <v-btn color="secondary" @click="openNewContactForm">
        Novo Contato
      </v-btn>
    </v-row>

    <v-row v-if="filteredContacts.length > 0" class="mt-4">
      <v-col cols="12" v-for="contact in filteredContacts" :key="contact.id">
        <ContactCard
          :contact="contact"
          @deleted="handleDeleted"
          @edit="openEditContactForm"
        />
      </v-col>
    </v-row>

    <v-row v-else justify="center">
      <EmptyContacts />
    </v-row>

    <ContactForm
      :value="dialogVisible"
      :contactId="editingContactId"
      @input="dialogVisible = $event"
      @saved="onContactSaved"
      @show-snackbar="showSnackbar"
    />

    <v-snackbar
      v-model="snackbar"
      :timeout="3000"
      :color="snackbarColor"
      top
      right
      elevation="2"
    >
      {{ snackbarText }}
      <v-btn color="white" text @click="snackbar = false">Fechar</v-btn>
    </v-snackbar>
  </v-container>
</template>

<script lang="ts">
import Vue from "vue";
import ContactCard from "@/components/ContactCard.vue";
import EmptyContacts from "@/components/EmptyContacts.vue";
import ContactForm from "@/components/ContactForm.vue";
import { Icontact } from "@/Interfaces/Contact";

export default Vue.extend({
  components: { ContactCard, EmptyContacts, ContactForm },
  data() {
    return {
      search: "",
      dialogVisible: false,
      editingContactId: null as string | null,
      snackbar: false,
      snackbarText: "",
      snackbarColor: "success",
    };
  },
  computed: {
    contacts(): Icontact[] {
      return this.$store.getters["contacts/contacts"];
    },
    filteredContacts(): Icontact[] {
      return this.contacts.filter((contact: Icontact) =>
        contact.name.toLowerCase().includes(this.search.toLowerCase())
      );
    },
  },
  created() {
    this.fetchContacts();
  },
  methods: {
    async fetchContacts() {
      try {
        await this.$store.dispatch("contacts/fetchContacts");
      } catch (error) {
        this.showSnackbar({
          message: "Erro ao carregar contatos",
          color: "error",
        });
      }
    },
    openNewContactForm() {
      this.editingContactId = null;
      this.dialogVisible = true;
    },
    openEditContactForm(id: string) {
      this.editingContactId = id;
      this.dialogVisible = true;
    },
    async onContactSaved() {
      this.dialogVisible = false;
      await this.fetchContacts();
      this.showSnackbar({
        message: "Contato salvo com sucesso!",
        color: "success",
      });
    },
    async handleDeleted(message: string) {
      await this.fetchContacts();
      this.showSnackbar({
        message,
        color: message.toLowerCase().includes("erro") ? "error" : "success",
      });
    },
    showSnackbar(payload: { message: string; color: string }) {
      this.snackbarText = payload.message;
      this.snackbarColor = payload.color;
      this.snackbar = true;
    },
  },
});
</script>
