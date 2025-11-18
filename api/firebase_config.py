import os

# Detectar si estamos en CI o si no existe la llave
IS_CI = os.getenv("CI") == "true"
SERVICE_KEY_PATH = os.path.join("config", "keys", "serviceAccountKey.json")

# Si estamos en CI o el archivo no existe → no inicializar firebase
if IS_CI or not os.path.exists(SERVICE_KEY_PATH):
    print("⚠️ Firebase Admin no inicializado (modo CI o llave faltante).")
    db = None
else:
    import firebase_admin
    from firebase_admin import credentials, firestore

    cred = credentials.Certificate(SERVICE_KEY_PATH)
    firebase_admin.initialize_app(cred)
    db = firestore.client()
