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
import pytest_asyncio
from collections.abc import AsyncGenerator
from httpx import AsyncClient, ASGITransport
from backend.main import app


# Fixture to create an AsyncClient for testing
@pytest_asyncio.fixture
async def test_client() -> AsyncGenerator[AsyncClient, None]:
    """Provides an AsyncClient connected to the FastAPI app for testing."""
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        yield client


@pytest.mark.asyncio
async def test_userdata(test_client: AsyncClient):
    """Test the /userdata POST endpoint."""
    payload = {
        "name": "test1",
        "email": "test1@klizos.com",
        "phone_no": 7063315080,
        "password": "Klizos@123"
    }

    # Send POST request
    response = await test_client.post("/userdata", json=payload)

    # Validate response
    assert response.status_code == 200
    data = response.json()
    assert data['msg'] == "User data entered"
    assert data['status'] is True
