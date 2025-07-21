<template>
  <v-app>
    <v-app-bar app>
      <v-toolbar-title>
        Fullstack SPA Challenge - Address Book (KNN)
      </v-toolbar-title>
    </v-app-bar>

    <v-main id="main-content">
      <router-view />
    </v-main>

    <v-snackbar
      v-model="$store.state.snackbar.show"
      :color="$store.state.snackbar.color"
      timeout="3000"
      top
      right
    >
      {{ $store.state.snackbar.message }}
    </v-snackbar>
  </v-app>
</template>

<style>
#main-content {
  margin-top: 2rem;
  background-color: whitesmoke;
}
</style>
