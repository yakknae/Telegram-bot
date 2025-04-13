# test_dolar_api.py
from app.dolar_api import get_dolar_price

def test_get_dolar_price():
    price = get_dolar_price()
    if price:
        print("Precio del Dólar Oficial:")
        print(f"Compra: ${price['compra']:.2f}")
        print(f"Venta: ${price['venta']:.2f}")
    else:
        print("No se pudo obtener el precio del dólar.")

if __name__ == "__main__":
    test_get_dolar_price()
