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

    <v-row v-if="showForm" class="mb-6">
      <v-col cols="12">
        <ContactForm
          :contactId="editingContactId"
          @saved="onContactSaved"
          @cancel="showForm = false"
        />
      </v-col>
    </v-row>

    <v-row v-else-if="filteredContacts.length > 0">
      <v-col cols="12" v-for="contact in filteredContacts" :key="contact.id">
        <ContactCard :Contact="contact" />
      </v-col>
    </v-row>

    <v-row v-else justify="center">
      <EmptyContacts />
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import ContactCard from "@/components/ContactCard.vue";
import EmptyContacts from "@/components/EmptyContacts.vue";
import ContactForm from "@/components/ContactForm.vue";
import { contact } from "@/Interfaces/Contact";
import axios from "axios";

export default defineComponent({
  components: { ContactCard, EmptyContacts, ContactForm },
  data() {
    return {
      search: "",
      showForm: false,
      editingContactId: null as string | null,
      contactsList: [] as contact[],
    };
  },
  computed: {
    filteredContacts(): contact[] {
      return this.contactsList.filter((contact) =>
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
        const { data } = await axios.get("/contacts");
        this.contactsList = data;
      } catch (error) {
        alert("Erro ao carregar contatos");
      }
    },
    openNewContactForm() {
      this.editingContactId = null;
      this.showForm = true;
    },
    async onContactSaved() {
      this.showForm = false;
      await this.fetchContacts();
      alert("Contato salvo com sucesso!");
    },
  },
});
</script>
