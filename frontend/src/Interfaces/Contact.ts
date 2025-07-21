export interface Icontact {
  id?: number;
  name: string;
  email: string;
  phone: string;
  cep: string;
  address: IContactAdress;
}

export interface IContactAdress {
  cep: string;
  logradouro: string;
  bairro: string;
  cidade: string;
  estado: string;
}
