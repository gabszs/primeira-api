import httpx
import random

def test_hello_world_endpoint():
    esperado = {"message": "Hello World!!"}
    resultado = httpx.get(
        "http://127.0.0.1:8000/hello_world"
    ).json()

    assert esperado == resultado


def test_soma_endpoint():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    esperado = {"message": num1 + num2}

    resultado = httpx.get(
        f"http://127.0.0.1:8000/soma/num1/{num1}/num2/{num2}"
    ).json()


    assert esperado == resultado
