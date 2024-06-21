# campaigns/views.py (do the same for characters/views.py and worlds/views.py)

from rest_framework import viewsets
from .models import Campaign
from .serializers import CampaignSerializer
from rest_framework.permissions import AllowAny  # Change this import

class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    permission_classes = [AllowAny]  # Change this line

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)