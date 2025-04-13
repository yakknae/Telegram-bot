from telegram.ext import ApplicationBuilder, CommandHandler, filters
from dotenv import load_dotenv
import os
from .commands import (
    help_command,
    language_command,
    money_command,
    back_command,
    set_language,
    euro_command,
    real_br_command,
    peso_chl_command,
    peso_uru_command,
    dolar_o_command,
    dolar_b_command,
)
from telegram.error import TimedOut

# Cargar variables de entorno
load_dotenv()

# Token (.env)
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
print(f"Token del bot cargado: {TELEGRAM_BOT_TOKEN}")  # Mensaje de depuración

# Función de manejo de errores global
async def error_handler(update, context):
    try:
        # Capturar errores específicos
        if isinstance(context.error, TimedOut):
            print("Error: Timeout al comunicarse con la API de Telegram.")
        else:
            print(f"Error no manejado: {context.error}")
    except Exception as e:
        print(f"Error en el manejador de errores: {e}")


def run_bot():
    try:
        print("Iniciando el bot...")  # Mensaje de depuración
        application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).connection_pool_size(8).read_timeout(30).write_timeout(30).build()
        
        # Registrar comandos
        application.add_handler(CommandHandler("help", help_command))
        application.add_handler(CommandHandler("language", language_command))
        application.add_handler(CommandHandler("money", money_command))
        application.add_handler(CommandHandler("back", back_command))
        application.add_handler(CommandHandler("es", lambda update, context: set_language(update, context, "es")))
        application.add_handler(CommandHandler("br", lambda update, context: set_language(update, context, "br")))
        application.add_handler(CommandHandler("en", lambda update, context: set_language(update, context, "en")))
        application.add_handler(CommandHandler("dolar_o", dolar_o_command))
        application.add_handler(CommandHandler("dolar_b", dolar_b_command))
        application.add_handler(CommandHandler("euro", euro_command))
        application.add_handler(CommandHandler("real_br", real_br_command))
        application.add_handler(CommandHandler("peso_chl", peso_chl_command))
        application.add_handler(CommandHandler("peso_uru", peso_uru_command))
        

        # Iniciar el bot
        application.run_polling()
    except KeyboardInterrupt:
        print("Bot detenido manualmente.")
    except Exception as e:
        print(f"Error crítico al iniciar el bot: {e}")
    finally:
        print("Cerrando el bot...")

if __name__ == "__main__":
    run_bot()