# dragonbyte_realms/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from campaigns.views import CampaignViewSet
from characters.views import CharacterViewSet
from worlds.views import WorldViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from user_auth.views import RegisterView, profile_view  # Import the profile view

router = DefaultRouter()
router.register(r'campaigns', CampaignViewSet)
router.register(r'characters', CharacterViewSet)
router.register(r'worlds', WorldViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('accounts/profile/', profile_view, name='profile'),  # Add this line
]
