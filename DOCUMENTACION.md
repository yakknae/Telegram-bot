---
#codigo manual para cargar los comandos de las monedas, ahora en el codigo vamos a utilizar uno optimizado
#Crear el comando para el dolar
async def dolar_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        tipo = "oficial"
        if context.args and context.args[0].lower() in  ["blue", "b"]:
            tipo = "blue"
        elif context.args and context.args[0].lower() in ["oficial", "o"]:
            tipo = "oficial"

        print(f"Comando /dolar recibido para {tipo}")  # Mensaje de depuración
        price = get_dolar_price(tipo)
        if price:
            message = (
                f"📊 Precio del Dólar {tipo.capitalize()}:\n"
                f"💵 Compra: ${price['compra']:.2f}\n"
                f"💰 Venta: ${price['venta']:.2f}"
            )
        else:
            message = "No se pudo obtener el precio del dólar. Inténtalo más tarde."
        
        print(f"Respuesta generada: {message}")  # Mensaje de depuración
        await update.message.reply_text(message)
    except Exception as e:
        print(f"Error en el comando /dolar: {e}")
        await update.message.reply_text("Ocurrió un error al procesar tu solicitud.")

#Crear el comando para el euro
async def euro_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        price = get_dolar_price("euro")
        if price:
            message = (
                f"📊 Precio del Euro:\n"
                f"💵 Compra: ${price['compra']:.2f}\n"
                f"💰 Venta: ${price['venta']:.2f}"
            )
        else:
            message = "No se pudo obtener el precio del euro. Inténtalo más tarde."
        await update.message.reply_text(message)
    except Exception as e:
        print(f"Error en el comando /euro: {e}")
        await update.message.reply_text("Ocurrió un error al procesar tu solicitud.")

#Crear el comando para el real brasilero
async def real_br_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        price = get_dolar_price("real_br")
        if price:
            message = (
                f"📊 Precio del real brasilero:\n"
                f"💵 Compra: ${price['compra']:.2f}\n"
                f"💰 Venta: ${price['venta']:.2f}"
            )
        else:
            message = "No se pudo obtener el precio del real brasilero. Inténtalo más tarde."
        await update.message.reply_text(message)
    except Exception as e:
        print(f"Error en el comando /real_br: {e}")
        await update.message.reply_text("Ocurrió un error al procesar tu solicitud.")

#Crear el comando para el peso chileno
async def peso_chl_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        price = get_dolar_price("peso_chl")
        if price:
            message = (
                f"📊 Precio del peso chileno:\n"
                f"💵 Compra: ${price['compra']:.2f}\n"
                f"💰 Venta: ${price['venta']:.2f}"
            )
        else:
            message = "No se pudo obtener el precio del peso chileno. Inténtalo más tarde."
        await update.message.reply_text(message)
    except Exception as e:
        print(f"Error en el comando /peso_chl: {e}")
        await update.message.reply_text("Ocurrió un error al procesar tu solicitud.")

#Crear el comando para el peso uruguayo
async def peso_uru_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        price = get_dolar_price("peso_uru")
        if price:
            message = (
                f"📊 Precio del peso uruguayo:\n"
                f"💵 Compra: ${price['compra']:.2f}\n"
                f"💰 Venta: ${price['venta']:.2f}"
            )
        else:
            message = "No se pudo obtener el precio del peso uruguayo. Inténtalo más tarde."
        await update.message.reply_text(message)
    except Exception as e:
        print(f"Error en el comando /peso_uru: {e}")
        await update.message.reply_text("Ocurrió un error al procesar tu solicitud.")
---
