<template>
  <v-container>
    <ContactForm :contactId="$route.params.id" />
  </v-container>
</template>

<script lang="ts">
import ContactForm from "@/components/ContactForm.vue";
export default {
  components: { ContactForm },
};
</script>
