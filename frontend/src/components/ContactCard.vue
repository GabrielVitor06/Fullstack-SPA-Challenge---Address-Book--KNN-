<template>
  <v-col cols="12" md="4">
    <v-card>
      <v-card-title>{{ Contact?.name }}</v-card-title>
      <v-card-text>
        <p>Email: {{ Contact?.email }}</p>
        <p>Telefone: {{ Contact?.phone }}</p>
        <p>
          Endereço: {{ Contact?.address.logradouro }},
          {{ Contact?.address.bairro }}, {{ Contact?.address.cidade }} -
          {{ Contact?.address.estado }}
        </p>
      </v-card-text>
      <v-card-actions>
        <v-btn
          text
          color="blue"
          @click="$router.push(`/contacts/${Contact.id}/edit`)"
        >
          Editar
        </v-btn>

        <v-btn text color="red" @click="deleteContact(Contact.id)">
          Excluir
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-col>
</template>

<script lang="ts">
import { contact } from "@/Interfaces/Contact";
import { mapActions } from "vuex";

export default {
  props: {
    Contact: {
      type: Object as () => contact,
      default: () => ({}),
      required: true,
    },
  },
  methods: {
    ...mapActions("contacts", ["deleteContact"]),
  },
};
</script>
