<template>
  <div>
    <v-card class="py-1 px-6 rounded-lg elevation-1">
      <v-row align="center" justify="space-between">
        <v-col>
          <v-card-title>{{ contact?.name }}</v-card-title>
          <v-card-subtitle>
            Contatos: {{ contact?.email }} - {{ contact?.phone }}
          </v-card-subtitle>
          <v-card-text>
            Endereço: {{ contact?.address.logradouro }},
            {{ contact?.address.bairro }}, {{ contact?.address.cidade }} -
            {{ contact?.address.estado }}
          </v-card-text>
        </v-col>

        <v-col class="d-flex flex-column align-end">
          <v-btn text color="blue" @click="$emit('edit', contact.id)">
            Editar
          </v-btn>

          <v-btn text color="red" @click="dialog = true">Excluir</v-btn>
        </v-col>
      </v-row>
    </v-card>

    <v-dialog v-model="dialog" max-width="400">
      <v-card>
        <v-card-title class="headline">Confirmar exclusão</v-card-title>
        <v-card-text>
          Você tem certeza que deseja excluir este contato?
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn text @click="dialog = false">Cancelar</v-btn>
          <v-btn text color="red" @click="confirmDelete">Excluir</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import { Icontact } from "@/Interfaces/Contact";
import { mapActions } from "vuex";

export default Vue.extend({
  props: {
    contact: {
      type: Object as () => Icontact,
      required: true,
    },
  },
  data() {
    return {
      dialog: false,
    };
  },
  methods: {
    ...mapActions("contacts", ["deleteContact"]),
    async confirmDelete() {
      this.dialog = false;
      try {
        await this.deleteContact(this.contact.id);
        this.$emit("deleted", "Contato excluído com sucesso!");
      } catch (error) {
        this.$emit("deleted", "Erro ao excluir contato: " + error);
      }
    },
  },
});
</script>
