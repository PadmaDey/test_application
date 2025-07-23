# import pytest
# from fastapi.testclient import TestClient
# from backend.main import app

# test_client = TestClient(app)

# @pytest.mark.asyncio
# async def test_userdata():
#     payload = {
#         "name": "test1",
#         "email": "test1@klizos.com",
#         "phone_no": 7063315080,
#         "password": "Klizos@123"
#     }
#     response = test_client.post("/userdata", json=payload)
#     assert response.status_code == 200

#     data = response.json()
#     assert data['msg'] == "User data entered"
#     assert data['status'] is True


import pytest
from httpx import AsyncClient
from backend.main import app

@pytest.mark.asyncio
async def test_userdata():
    payload = {
        "name": "test1",
        "email": "test1@klizos.com",
        "phone_no": 7063315080,
        "password": "Klizos@123"
    }
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/userdata", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data['msg'] == "User data entered"
    assert data['status'] is True
