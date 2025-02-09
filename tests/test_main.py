import random

import pytest


@pytest.mark.asyncio
async def test_hello_world_endpoint(client):
    esperado = {"message": "Hello World!!"}

    resultado = await client.get("http://127.0.0.1:8000/hello_world")
    assert esperado == resultado.json()


@pytest.mark.asyncio
async def test_soma_endpoint(client):
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    esperado = {"message": num1 + num2}

    resultado = await client.get(f"http://127.0.0.1:8000/soma/num1/{num1}/num2/{num2}")

    assert esperado == resultado.json()
