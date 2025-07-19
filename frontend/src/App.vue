<template>
  <v-app>
    <v-app-bar app>
      <v-toolbar-title
        >Fullstack SPA Challenge - Address Book (KNN)</v-toolbar-title
      >
    </v-app-bar>
    <v-main id="main-content">
      <router-view />
    </v-main>
  </v-app>
</template>

<style>
#main-content {
  margin-top: 2rem;
  background-color: whitesmoke;
}
</style>
