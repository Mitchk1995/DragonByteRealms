# campaigns/models.py

from django.db import models
from django.conf import settings

class Campaign(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class CharacterCampaignState(models.Model):
    character = models.ForeignKey('characters.Character', on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    character_class = models.CharField(max_length=50)
    level = models.IntegerField(default=1)
    experience = models.IntegerField(default=0)
    hit_points = models.IntegerField(default=10)
    armor_class = models.IntegerField(default=10)
    
    class Meta:
        unique_together = ('character', 'campaign')

    def __str__(self):
        return f"{self.character.name} in {self.campaign.title}"

class NPC(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    campaign = models.ForeignKey(Campaign, related_name='npcs', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Quest(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    campaign = models.ForeignKey(Campaign, related_name='quests', on_delete=models.CASCADE)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title