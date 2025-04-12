from fastapi import FastAPI
from dolar_api import get_dolar_price

app = FastAPI()

@app.get("/dolar")
def get_dolar():
    price = get_dolar_price()
    if price:
        return {
            "compra": price["compra"],
            "venta": price["venta"]
        }
    else:
        return {"error": "No se pudo obtener el precio del dólar"}