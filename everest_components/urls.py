from django.urls import path
from .views import LatestReceivedDataAPIView

urlpatterns = [
    # Other URL patterns...
    path('/me/', LatestReceivedDataAPIView.as_view(), name='latest_received_data_api'),
]
