<template>
  <v-container>
    <v-row justify="space-between">
      <h1>Contatos</h1>
      <v-btn color="primary" @click="$router.push('/contacts/new')"
        >Novo Contato</v-btn
      >
    </v-row>
    <v-row>
      <ContactCard
        v-for="contact in contacts"
        :key="contact.id"
        :contact="contact"
      />
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { mapGetters, mapActions } from "vuex";
import ContactCard from "@/components/ContactCard.vue";

export default defineComponent({
  components: { ContactCard },
  computed: {
    ...mapGetters("contacts", ["contacts"]),
  },
  created() {
    // Força o TypeScript a entender que isso será definido em runtime
    (this as any).fetchContacts();
  },
  methods: {
    ...mapActions("contacts", ["fetchContacts"]),
  },
});
</script>
