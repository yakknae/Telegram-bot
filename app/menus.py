# app/menus.py

menus = {
    "main": {
        "es": (
            "Menú Principal:\n"
            "/language - Cambiar idioma.\n"
            "/money - Ver opciones de monedas.\n"
        ),
        "br": (
            "Menu Principal:\n"
            "/language - Mudar idioma.\n"
            "/money - Ver opções de moedas.\n"
        ),
        "en": (
            "Main Menu:\n"
            "/language - Change language.\n"
            "/money - View currency options.\n"
        ),
    },
################################################
    "language": {
        "es": (
            "Selecciona un idioma:\n"
            "/es - Español.\n"
            "/br - Portugués (Brasil).\n"
            "/en - Inglés.\n"
            "/back - Volver al menú principal."
        ),
        "br": (
            "Selecione um idioma:\n"
            "/es - Espanhol.\n"
            "/br - Português (Brasil).\n"
            "/en - Inglês.\n"
            "/back - Voltar ao menu principal."
        ),
        "en": (
            "Select a language:\n"
            "/es - Spanish.\n"
            "/br - Portuguese (Brazil).\n"
            "/en - English.\n"
            "/back - Go back to the main menu."
        ),
    },
################################################
    "money": {
        "es": (
            "Selecciona una moneda:\n"
            "/dolar_o - Dólar oficial.\n"
            "/dolar_b - Dólar blue.\n"
            "/euro - Euro.\n"
            "/real_br - Real brasileño.\n"
            "/peso_chl - Peso chileno.\n"
            "/peso_uru - Peso uruguayo.\n"
            "/back - Volver al menú principal."
        ),
        "br": (
            "Selecione uma moeda:\n"
            "/dolar_o - Dólar oficial.\n"
            "/dolar_b - Dólar blue.\n"
            "/euro - Euro.\n"
            "/real_br - Real brasileiro.\n"
            "/peso_chl - Peso chileno.\n"
            "/peso_uru - Peso uruguaio.\n"
            "/back - Voltar ao menu principal."
        ),
        "en": (
            "Select a currency:\n"
            "/dolar_o - Official dollar.\n"
            "/dolar_b - Blue dollar.\n"
            "/euro - Euro.\n"
            "/real_br - Brazilian real.\n"
            "/peso_chl - Chilean peso.\n"
            "/peso_uru - Uruguayan peso.\n"
            "/back - Go back to the main menu."
        ),
    },
 "price": {
        "es": {
            "price_message": "🏦 Precio del {currency}:\n"
                             "💵 Compra: ${buy:.2f}\n"
                             "💰 Venta: ${sell:.2f}",
            "not_found": "No se pudo obtener el precio del {currency}.",
        },
        "br": {
            "price_message": "🏦 Preço do {currency}:\n"
                             "💵 Compra: ${buy:.2f}\n"
                             "💰 Venda: ${sell:.2f}",
            "not_found": "Não foi possível obter o preço do {currency}.",
        },
        "en": {
            "price_message": "🏦 {currency} Price:\n"
                             "💵 Buy: ${buy:.2f}\n"
                             "💰 Sell: ${sell:.2f}",
            "not_found": "Could not get the price of {currency}.",
        },
    },
################################################
    "errors": {
        "es": "Ocurrió un error al procesar tu solicitud.",
        "br": "Ocorreu um erro ao processar sua solicitação.",
        "en": "An error occurred while processing your request.",
    },
################################################
    "currency_not_found": {
        "es": "No se pudo obtener el precio del {currency}. Inténtalo más tarde.",
        "br": "Não foi possível obter o preço do {currency}. Tente novamente mais tarde.",
        "en": "Could not get the price of the {currency}. Try again later.",
    },
}