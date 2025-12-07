from api.firebase_config import db
import pytz

def get_alerts():
    alerts_ref = db.collection("alerts")
    docs = alerts_ref.stream()
    alerts = []
    
    for doc in docs:
        data = doc.to_dict()
        created_at_obj = data.get("createdAt") 
        created_at_seconds = None 
        
        
        if created_at_obj and hasattr(created_at_obj, 'timestamp'):
            created_at_seconds = int(created_at_obj.timestamp())
        
        status_raw = data.get("status", "En Proceso").lower()
        if status_raw in ["en proceso", "active", "activo"]:
            final_status = "En Proceso"
        elif status_raw in ["resuelto", "resolved", "finalizado"]:
            final_status = "Resuelto"
        else:
            final_status = "En Proceso" 

        alerts.append({
            "id": doc.id,
            "title": data.get("title"),
            "description": data.get("description"),
            "alertType": data.get("alertType"),
            
            "status": final_status,
            
            "imageUrl": data.get("imageUrl"), 
            "latitude": data.get("latitude") or data.get("location", {}).get("latitude"),
            "longitude": data.get("longitude") or data.get("location", {}).get("longitude"),
            
            
            "createdAtSeconds": created_at_seconds,
        })
    
    return alerts