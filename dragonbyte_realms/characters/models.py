# characters/models.py

from django.db import models
from django.conf import settings

class Character(models.Model):
    name = models.CharField(max_length=100)
    race = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    # Basic attributes
    strength = models.IntegerField(default=10)
    dexterity = models.IntegerField(default=10)
    constitution = models.IntegerField(default=10)
    intelligence = models.IntegerField(default=10)
    wisdom = models.IntegerField(default=10)
    charisma = models.IntegerField(default=10)
    
    # Background
    background = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.race}"

class Skill(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    character = models.ForeignKey(Character, related_name='skills', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class InventoryItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField(default=1)
    character = models.ForeignKey(Character, related_name='inventory', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} (x{self.quantity})"