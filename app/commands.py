# app/commands.py
from telegram import Update
from telegram.ext import ContextTypes
from .utils import get_user_language, user_language, get_user_state, set_user_state
from .dolar_api import get_dolar_price
from .menus import menus

# Función genérica para cambiar el idioma
async def set_language(update: Update, context: ContextTypes.DEFAULT_TYPE, language_code: str):
    # Validar que update.message exista
    if not update.message:
        return

    user_id = update.message.from_user.id

    if language_code in ["es", "br", "en"]:
        # Guardar el idioma seleccionado
        user_language[user_id] = language_code
        # Establecer el estado del usuario como "main"
        set_user_state(user_id, "money")
        # Mostrar directamente la lista de monedas
        message = menus["money"][language_code]
    else:
        message = "Idioma no soportado. Usa /es, /br o /en."

    await update.message.reply_text(message)

# Comando /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Validar que update.message exista
    if not update.message:
        return

    user_id = update.message.from_user.id
    lang = get_user_language(user_id)  # Obtener el idioma del usuario

    # Usar un idioma predeterminado si lang no es válido
    if lang not in ["es", "br", "en"]:
        lang = "es"


    message = menus["main"]["es"]  # Usar el idioma predeterminado (español)
    set_user_state(user_id, "initial")  # Asegurarse de que el estado sea "initial"

    await update.message.reply_text(message)


# Comando /language
async def language_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Validar que update.message exista
    if not update.message:
        return

    user_id = update.message.from_user.id
    lang = get_user_language(user_id)  # Obtener el idioma del usuario

    # Usar un idioma predeterminado si lang no es válido
    if lang not in ["es", "br", "en"]:
        lang = "es"

    # Establecer el estado del usuario como "language"
    set_user_state(user_id, "language")
    message = menus["language"][lang]
    await update.message.reply_text(message)

# Comando /money
async def money_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Validar que update.message exista
    if not update.message:
        return

    user_id = update.message.from_user.id
    lang = get_user_language(user_id)

    # Usar un idioma predeterminado si lang no es válido
    if lang not in ["es", "br", "en"]:
        lang = "es"

    # Establecer el estado del usuario como "money"
    set_user_state(user_id, "money")
    message = menus["money"][lang]

    await update.message.reply_text(message)

# Comando /back
async def back_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Validar que update.message exista
    if not update.message:
        return

    user_id = update.message.from_user.id
    lang = get_user_language(user_id)

    # Usar un idioma predeterminado si lang no es válido
    if lang not in ["es", "br", "en"]:
        lang = "es"

    # Obtener el estado actual del usuario
    current_state = get_user_state(user_id)
    print(f"Estado actual del usuario {user_id} antes de /back: {current_state}")

    if current_state == "language":
        # Volver al menú anterior desde /language
        set_user_state(user_id, "main")  # Volver al menú inicial
        message = menus["main"]["es"]
    elif current_state == "money":
        # Volver al menú anterior desde /money
        set_user_state(user_id, "main")  # Volver al menú principal
        message = menus["main"][lang]
    else:
        # Si ya está en el menú principal, mostrar mensaje de error
        message = menus["errors"][lang]

    await update.message.reply_text(message)

# Función genérica para manejar comandos de monedas
async def currency_command(update: Update, context: ContextTypes.DEFAULT_TYPE, currency_type: str, currency_name: str):
    try:
        # Validar que update.message exista
        if not update.message:
            return

        user_id = update.message.from_user.id
        lang = get_user_language(user_id)

        # Usar un idioma predeterminado si lang no es válido
        if lang not in ["es", "br", "en"]:
            lang = "es"

        print(f"Comando /{currency_name} recibido")  # Mensaje de depuración
        price = get_dolar_price(currency_type)
        if price:
            message_template = menus["price"][lang]["price_message"]
            message = message_template.format(
                currency = currency_name.capitalize(),
                buy=price['compra'],
                sell=price['venta']
            )
        else:
            message_template = menus["price"][lang]["not_found"]
            message = message_template.format(currency=currency_name)

        print(f"Respuesta generada: {message}")  # Mensaje de depuración
        await update.message.reply_text(message)

        set_user_state(user_id,"money")
        menu_message = menus["money"][lang]
        await update.message.reply_text(menu_message)

    except Exception as e:
        print(f"Error en el comando /{currency_name}: {e}")
        # Asegurarse de que lang esté definido incluso si ocurre un error
        lang = get_user_language(user_id) if 'user_id' in locals() else "es"
        await update.message.reply_text(menus["errors"][lang])

# Crear funciones específicas usando la función genérica
async def dolar_o_command(update:Update, context: ContextTypes.DEFAULT_TYPE):
    await currency_command(update, context, "oficial", "Dolar Oficial")

async def dolar_b_command(update:Update, context: ContextTypes.DEFAULT_TYPE):
    await currency_command(update, context, "blue", "Dolar Blue")

async def euro_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await currency_command(update, context, "euro", "Euro")

async def real_br_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await currency_command(update, context, "real_br", "Real Brasileño")

async def peso_chl_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await currency_command(update, context, "peso_chl", "Peso Chileno")

async def peso_uru_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await currency_command(update, context, "peso_uru", "Peso Uruguayo")