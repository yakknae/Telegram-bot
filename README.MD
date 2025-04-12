# Telegram Bot

Un bot de Telegram para realizar conversiones de monedas globales.

## Características
- Conversión de múltiples monedas (ARS, EUR, USD, etc.).
- Soporte para varios idiomas (ES, EN, BR, etc.).
- Integración con DolarApi para tasas de cambio en tiempo real.

## instalar las dependencias
> pip install -r requirements.txt

## Configuración
1. Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:

   ```plaintext
- Reemplaza tu_token_de_telegram con tu token de Telegram.

   TELEGRAM_BOT_TOKEN=tu_token_de_telegram

## Comando inicializar bot
> python -m app.bot
