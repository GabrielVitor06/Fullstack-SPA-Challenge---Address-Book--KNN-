import { contact } from "@/Interfaces/Contact";

export function createEmptyContact(): contact {
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

export function formatContact(data: contact): contact {
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
  addressData: any,
  cep?: string
): contact["address"] {
  return {
    logradouro: addressData?.logradouro || "",
    bairro: addressData?.bairro || "",
    cidade: addressData?.cidade || "",
    estado: addressData?.estado || "",
    cep: cep || "",
  };
}
