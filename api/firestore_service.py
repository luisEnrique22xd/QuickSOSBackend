from api.firebase_config import db
from datetime import datetime, timedelta

def get_alerts():
    alerts_ref = db.collection("alerts")
    docs = alerts_ref.stream()
    alerts = []
    for doc in docs:
        data = doc.to_dict()
        alerts.append({
            "id": doc.id,
            "title": data.get("title"),
            "description": data.get("description"),
            "alertType": data.get("alertType"),
            "status": data.get("status"),
            "imageUrl": data.get("imageUrl"),
            "latitude": data.get("location", {}).get("latitude"),
            "longitude": data.get("location", {}).get("longitude"),
            "createdAt": data.get("createdAt"),
        })
    return alerts

