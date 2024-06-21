# worlds/serializers.py
from rest_framework import serializers
from .models import World

class WorldSerializer(serializers.ModelSerializer):
    class Meta:
        model = World
        fields = ['id', 'name', 'description', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']