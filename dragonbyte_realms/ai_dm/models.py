# ai_dm/models.py
from django.db import models
from campaigns.models import Campaign

class GameSession(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    session_log = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Session for {self.campaign.title} at {self.created_at}"