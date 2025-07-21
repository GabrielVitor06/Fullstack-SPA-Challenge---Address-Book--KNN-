declare module "v-mask" {
  import { PluginFunction } from "vue";

  const VMask: {
    install: PluginFunction<unknown>;
  };

  export default VMask;
}
