import requests

def get_dolar_price(tipo="oficial"):
    try:
        # Mapear los tipos de dólar a los endpoints correspondientes
        endpoints = {
            "oficial": "https://dolarapi.com/v1/dolares/oficial",
            "blue": "https://dolarapi.com/v1/dolares/blue",
            "euro": "https://dolarapi.com/v1/cotizaciones/eur",
            "real_br": "https://dolarapi.com/v1/cotizaciones/brl",
            "peso_chl": "https://dolarapi.com/v1/cotizaciones/clp",
            "peso_uru": "https://dolarapi.com/v1/cotizaciones/uyu"
        }
        
        # Obtener el endpoint correspondiente al tipo solicitado
        url = endpoints.get(tipo.lower())
        if not url:
            print(f"Tipo de dólar no soportado: {tipo}")
            return None
        
        # Realizar la solicitud HTTP
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

       # Extraer los valores de compra y venta
        compra = data['compra']
        venta = data['venta']
        
        return {
            "compra": float(compra),
            "venta": float(venta)
        }
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión: {e}")
    except Exception as e:
        print(f"Error al procesar los datos: {e}")
    
    return None