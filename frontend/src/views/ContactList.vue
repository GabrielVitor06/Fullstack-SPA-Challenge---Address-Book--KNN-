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
          @deleted="fetchContacts"
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
    />
  </v-container>
</template>

<script lang="ts">
import Vue from "vue";
import ContactCard from "@/components/ContactCard.vue";
import EmptyContacts from "@/components/EmptyContacts.vue";
import ContactForm from "@/components/ContactForm.vue";
import { contact } from "@/Interfaces/Contact";

export default Vue.extend({
  components: { ContactCard, EmptyContacts, ContactForm },
  data() {
    return {
      search: "",
      dialogVisible: false,
      editingContactId: null as string | null,
    };
  },
  computed: {
    contacts(): contact[] {
      return this.$store.getters["contacts/contacts"];
    },
    filteredContacts(): contact[] {
      return this.contacts.filter((contact: contact) =>
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
        alert("Erro ao carregar contatos");
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
      alert("Contato salvo com sucesso!");
    },
  },
});
</script>
