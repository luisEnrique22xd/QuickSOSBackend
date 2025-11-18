from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.firestore_service import get_alerts

# Create your views here.
class AlertListView(APIView):
    def get(self, request):
        alerts = get_alerts()
        return Response(alerts, status=status.HTTP_200_OK)