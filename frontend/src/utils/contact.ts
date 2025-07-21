/* eslint-disable @typescript-eslint/no-explicit-any */
import { Icontact } from "@/Interfaces/Contact";

const defaultContact: Icontact = {
  id: undefined,
  name: "",
  email: "",
  phone: "",
  cep: "",
  address: {
    cep: "",
    logradouro: "",
    bairro: "",
    cidade: "",
    estado: "",
  },
};

function deepMerge<T>(target: T, source: Partial<T>): T {
  for (const key in source) {
    const sourceValue = source[key];
    const targetValue = target[key];

    if (
      sourceValue &&
      typeof sourceValue === "object" &&
      !Array.isArray(sourceValue)
    ) {
      if (targetValue && typeof targetValue === "object") {
        target[key] = deepMerge(targetValue, sourceValue as Partial<any>);
      } else {
        target[key] = sourceValue as any;
      }
    } else if (sourceValue !== undefined) {
      target[key] = sourceValue as any;
    }
  }

  return target;
}

export function createEmptyContact(): Icontact {
  return JSON.parse(JSON.stringify(defaultContact));
}

export function formatContact(data: Partial<Icontact>): Icontact {
  return deepMerge(createEmptyContact(), data);
}
