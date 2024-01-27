# everest_broker/urls.py
from django.urls import path
from .views import receive_post, live_data, delete_all_data

urlpatterns = [
    path('receive_post/', receive_post, name='receive_post'),
    path('', live_data, name='live_data'),
    path('delete_all_data/', delete_all_data, name='delete_all_data'),
    # Add other URL patterns as needed
]
