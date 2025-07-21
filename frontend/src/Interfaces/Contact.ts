export interface Icontact {
  id?: number;
  name: string;
  email: string;
  phone: string;
  cep: string;
  address: IcontactAdress;
}

export interface IcontactAdress {
  cep: string;
  logradouro: string;
  bairro: string;
  cidade: string;
  estado: string;
}
