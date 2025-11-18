from django.contrib import admin
from django.urls import path
from api.views import AlertListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/alerts/', AlertListView.as_view(), name='alerts'),
]
