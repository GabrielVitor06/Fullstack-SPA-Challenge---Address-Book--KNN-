import { Icontact } from "@/Interfaces/Contact";

export function createEmptyContact(): Icontact {
  return {
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
}

export function formatContact(data: Icontact): Icontact {
  return {
    id: data.id,
    name: data.name || "",
    email: data.email || "",
    phone: data.phone || "",
    cep: data.cep || "",
    address: formatAddress(data.address, data.cep),
  };
}

export function formatAddress(
  addressData: {
    logradouro?: string;
    bairro?: string;
    cidade?: string;
    estado?: string;
  } = {},
  cep?: string
): Icontact["address"] {
  return {
    logradouro: addressData?.logradouro || "",
    bairro: addressData?.bairro || "",
    cidade: addressData?.cidade || "",
    estado: addressData?.estado || "",
    cep: cep || "",
  };
}
