<template>
  <v-card class="py-3 px-6 rounded-lg elevation-1">
    <v-row align="center" justify="space-between">
      <v-col cols="9">
        <div class="text-subtitle-1 font-weight-medium">
          {{ Contact?.name }}
        </div>
        <div class="text-body-2">
          Contatos: {{ Contact?.email }} - {{ Contact?.phone }}
        </div>
        <div class="text-body-2">
          Endereço: {{ Contact?.address.logradouro }},
          {{ Contact?.address.bairro }}, {{ Contact?.address.cidade }} -
          {{ Contact?.address.estado }}
        </div>
      </v-col>

      <v-col cols="3" class="d-flex flex-column align-end">
        <v-btn
          text
          color="blue"
          class="mb-1"
          @click="$router.push(`/contacts/${Contact.id}/edit`)"
        >
          Editar
        </v-btn>
        <v-btn text color="red" @click="deleteContact(Contact.id)">
          Excluir
        </v-btn>
      </v-col>
    </v-row>
  </v-card>
</template>

<script lang="ts">
import { contact } from "@/Interfaces/Contact";
import { mapActions } from "vuex";

export default {
  props: {
    Contact: {
      type: Object as () => contact,
      required: true,
    },
  },
  methods: {
    ...mapActions("contacts", ["deleteContact"]),
  },
};
</script>
