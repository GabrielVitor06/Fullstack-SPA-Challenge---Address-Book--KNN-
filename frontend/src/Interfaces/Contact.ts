export interface contact {
  id?: number;
  name: string;
  email: string;
  phone: string;
  cep: string;
  address: {
    cep: string;
    logradouro: string;
    bairro: string;
    cidade: string;
    estado: string;
  };
}
