# urls.py
from django.urls import path, include
from .views import custom_token_obtain_pair, LogoutView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    # ... other paths
    path('token/', custom_token_obtain_pair, name='token_obtain_pair'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
