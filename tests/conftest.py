from typing import AsyncGenerator

import pytest_asyncio
from httpx import ASGITransport
from httpx import AsyncClient

from main import app


@pytest_asyncio.fixture
async def client() -> AsyncGenerator:
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="https://test"
    ) as client:
        yield client
