from fastapi import FastAPI

app: FastAPI = FastAPI()


@app.get("/hello_world")
async def hello_world():
    return {"message": "Hello World!!"}


# http://127.0.0.1:8000/soma/num1/7/num2/3
@app.get("/soma/num1/{num1}/num2/{num2}")
async def soma(num1: float, num2: float):
    resultado = num1 + num2
    return {"message": resultado}
