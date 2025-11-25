import os
import json
import firebase_admin
from firebase_admin import credentials, firestore

# --- Intentar inicializar Firebase SOLO si no está inicializado ---
if not firebase_admin._apps:

    # Detectar si estamos en Railway usando variables de entorno
    firebase_env = os.getenv("FIREBASE_SERVICE_KEY")

    if firebase_env:  
        print("🔥 Inicializando Firebase desde variables de entorno (Railway)")

        # Convertir string del JSON a dict
        cred_dict = json.loads(firebase_env)

        # Corregir salto de línea en private_key si viene roto
        if "private_key" in cred_dict:
            cred_dict["private_key"] = cred_dict["private_key"].replace("\\n", "\n")

        cred = credentials.Certificate(cred_dict)
        firebase_admin.initialize_app(cred)

    else:
        # Modo local usando archivo .json
        SERVICE_KEY_PATH = os.path.join("config", "keys", "serviceAccountKey.json")

        if os.path.exists(SERVICE_KEY_PATH):
            print("🔥 Inicializando Firebase desde archivo local")
            cred = credentials.Certificate(SERVICE_KEY_PATH)
            firebase_admin.initialize_app(cred)
        else:
            print("⚠️ Firebase NO inicializado (no existe archivo ni variable FIREBASE_SERVICE_KEY)")
            db = None
            exit()

# Crear cliente Firestore
db = firestore.client()
