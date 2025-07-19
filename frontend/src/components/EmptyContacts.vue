<template>
  <div class="empty-contacts">
    <font-awesome-icon :icon="['fas', 'user-slash']" size="4x" />

    <p>Nenhum contato encontrado.</p>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "EmptyContacts",
});
</script>

<style scoped>
.empty-contacts {
  text-align: center;
  padding: 40px 20px;
  color: #666;
  font-size: 1.3rem;
  font-style: italic;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.icon {
  margin-bottom: 16px;
  color: #999;
}
</style>
