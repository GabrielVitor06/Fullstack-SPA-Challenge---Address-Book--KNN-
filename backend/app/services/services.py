import httpx
from fastapi import HTTPException

async def get_address_from_cep(cep: str) -> dict:
    cep_clean = cep.replace("-", "")
    url = f"https://viacep.com.br/ws/{cep_clean}/json/"

    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
    
    if resp.status_code != 200:
        raise HTTPException(status_code=400, detail="Erro ao consultar ViaCEP")
    
    data = resp.json()
    if "erro" in data:
        raise HTTPException(status_code=422, detail="CEP inválido ou não encontrado")

    return {
        "logradouro": data.get("logradouro", ""),
        "bairro": data.get("bairro", ""),
        "cidade": data.get("localidade", ""),
        "estado": data.get("uf", ""),
    }
