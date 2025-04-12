user_language = {}
user_state = {}

# Obtener el idioma del usuario
def get_user_language(user_id):
    """
    Obtiene el idioma del usuario basado en su ID.
    Si no hay un idioma seleccionado, devuelve 'es' (español) como predeterminado.
    """
    return user_language.get(user_id, "es")  # Español por defecto

def get_user_state(user_id):
    """
    Obtiene el estado actual del usuario.
    Si no hay un estado, devuelve 'main' (menú principal) como predeterminado.
    """
    state = user_state.get(user_id, "main")
    print(f"Estado obtenido para el usuario {user_id}: {state}")
    return state

def set_user_state(user_id, state):
    """
    Establece el estado actual del usuario.
    """
    user_state[user_id] = state
    print(f"Estado establecido para el usuario {user_id}: {state}")