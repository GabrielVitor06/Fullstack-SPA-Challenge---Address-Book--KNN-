import { Module } from "vuex";

type SnackbarState = {
  show: boolean;
  message: string;
  color: "success" | "error" | "info" | "warning";
};

const snackbarModule: Module<SnackbarState, unknown> = {
  namespaced: true,
  state: {
    show: false,
    message: "",
    color: "success",
  },
  mutations: {
    showSnackbar(
      state,
      payload: { message: string; color: SnackbarState["color"] }
    ) {
      state.message = payload.message;
      state.color = payload.color;
      state.show = true;
    },
    hideSnackbar(state) {
      state.show = false;
    },
  },
  actions: {
    triggerSnackbar(
      { commit },
      payload: { message: string; color?: SnackbarState["color"] }
    ) {
      commit("showSnackbar", {
        message: payload.message,
        color: payload.color || "success",
      });
      setTimeout(() => {
        commit("hideSnackbar");
      }, 3000);
    },
  },
};

export default snackbarModule;
