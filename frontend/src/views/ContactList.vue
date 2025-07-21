<template>
  <v-container>
    <v-row justify="space-between" align="center">
      <v-col class="d-flex align-center" style="gap: 2rem">
        <h2>Contatos</h2>
        <v-text-field v-model="search" label="Buscar por nome" dense />
      </v-col>
      <v-col cols="12" sm="auto" class="d-flex justify-sm-end">
        <v-btn color="secondary" @click="goToNewContact" block>
          Novo Contato
        </v-btn>
      </v-col>
    </v-row>

    <v-row v-if="filteredContacts.length > 0" class="mt-4">
      <v-col cols="12" v-for="contact in filteredContacts" :key="contact.id">
        <ContactCard
          :contact="contact"
          @deleted="handleDeleted"
          @edit="goToEditContact"
        />
      </v-col>
    </v-row>

    <v-row v-else justify="center">
      <EmptyContacts />
    </v-row>
  </v-container>
</template>

<script lang="ts">
import Vue from "vue";
import ContactCard from "@/components/ContactCard.vue";
import EmptyContacts from "@/components/EmptyContacts.vue";
import { Icontact } from "@/Interfaces/Contact";

export default Vue.extend({
  name: "ContactsList",
  components: { ContactCard, EmptyContacts },
  data() {
    return {
      search: "" as string,
    };
  },
  computed: {
    contacts(): Icontact[] {
      return this.$store.getters["contacts/contacts"];
    },
    filteredContacts(): Icontact[] {
      return this.contacts.filter(
        (contact: Icontact) =>
          contact.name &&
          contact.name.toLowerCase().includes(this.search.toLowerCase())
      );
    },
  },
  async created() {
    try {
      await this.fetchContacts();
    } catch {
      this.triggerSnackbar("Erro ao carregar contatos", "error");
    }
  },
  methods: {
    async fetchContacts() {
      try {
        await this.$store.dispatch("contacts/fetchContacts");
      } catch {
        this.triggerSnackbar("Erro ao carregar contatos", "error");
      }
    },
    goToNewContact() {
      this.$router.push("/contacts/new");
    },
    goToEditContact(id: number | string) {
      const idNumber = typeof id === "string" ? Number(id) : id;
      this.$router.push(`/contacts/${idNumber}/edit`);
    },
    async handleDeleted(message: string) {
      await this.fetchContacts();
      const color = message.toLowerCase().includes("erro")
        ? "error"
        : "success";
      this.triggerSnackbar(message, color);
    },
    triggerSnackbar(
      message: string,
      color: "success" | "error" | "info" | "warning"
    ) {
      this.$store.dispatch("snackbar/triggerSnackbar", { message, color });
    },
  },
});
</script>
