import pytest
from httpx import AsyncClient

BASE_URL = "http://localhost:8000/api/v1"

@pytest.mark.asyncio
async def test_list_contacts():
    async with AsyncClient(base_url=BASE_URL) as ac:
        response = await ac.get("/contacts")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_create_contact():
    contact_data = {
        "name": "Teste User",
        "email": "testeuser@example.com",
        "phone": "123456789",
        "cep": "01001-000"
    }
    async with AsyncClient(base_url=BASE_URL) as ac:
        response = await ac.post("/contacts", json=contact_data)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == contact_data["name"]
    assert "logradouro" in data or "address" in data


@pytest.mark.asyncio
async def test_get_contact_by_id():
    contact_data = {
        "name": "Get User",
        "email": "getuser@example.com",
        "phone": "111222333",
        "cep": "01001-000"
    }
    async with AsyncClient(base_url=BASE_URL) as ac:
        create_resp = await ac.post("/contacts", json=contact_data)
        contact_id = create_resp.json()["id"]

        get_resp = await ac.get(f"/contacts/{contact_id}")
    assert get_resp.status_code == 200
    assert get_resp.json()["id"] == contact_id

@pytest.mark.asyncio
async def test_update_contact():
    contact_data = {
        "name": "Update User",
        "email": "updateuser@example.com",
        "phone": "987654321",
        "cep": "01001-000"
    }
    async with AsyncClient(base_url=BASE_URL) as ac:
        create_resp = await ac.post("/contacts", json=contact_data)
        contact_id = create_resp.json()["id"]

        update_data = {
            "name": "User Updated",
            "email": "updateuser@example.com",
            "phone": "000000000",
            "cep": "01001-000"
        }
        update_resp = await ac.put(f"/contacts/{contact_id}", json=update_data)
    assert update_resp.status_code == 200
    assert update_resp.json()["name"] == "User Updated"

@pytest.mark.asyncio
async def test_delete_contact():
    contact_data = {
        "name": "Delete User",
        "email": "deleteuser@example.com",
        "phone": "555555555",
        "cep": "01001-000"
    }
    async with AsyncClient(base_url=BASE_URL) as ac:
        create_resp = await ac.post("/contacts", json=contact_data)
        contact_id = create_resp.json()["id"]

        del_resp = await ac.delete(f"/contacts/{contact_id}")
        assert del_resp.status_code == 204

        get_resp = await ac.get(f"/contacts/{contact_id}")
        assert get_resp.status_code == 404
