

from typing import AsyncGenerator
from httpx import ASGITransport
from httpx import AsyncClient
import pytest_asyncio
from main import app
import pytest


@pytest_asyncio.fixture
async def client() -> AsyncGenerator:
    async with AsyncClient(transport=ASGITransport(app=app), base_url="https://test") as client:
        yield client