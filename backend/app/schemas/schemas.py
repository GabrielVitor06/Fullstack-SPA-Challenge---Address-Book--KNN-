from pydantic import BaseModel, EmailStr, Field, constr

cep_regex = r'^\d{5}-?\d{3}$'


class Address(BaseModel):
    cep: str
    logradouro: str
    bairro: str
    cidade: str
    estado: str


class ContactBase(BaseModel):
    name: constr(max_length=100)  # type: ignore
    email: EmailStr
    phone: str | None = None
    cep: str = Field(..., pattern=cep_regex)


class ContactCreate(ContactBase):
    pass


class ContactUpdate(ContactBase):
    pass


class ContactResponse(ContactBase):
    id: int
    address: Address

    model_config = dict(from_attributes=True)
