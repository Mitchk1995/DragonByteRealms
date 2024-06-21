# campaigns/serializers.py

from rest_framework import serializers
from .models import Campaign, NPC, Quest, CharacterCampaignState

class NPCSerializer(serializers.ModelSerializer):
    class Meta:
        model = NPC
        fields = ['id', 'name', 'description']

class QuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quest
        fields = ['id', 'title', 'description', 'is_complete']

class CharacterCampaignStateSerializer(serializers.ModelSerializer):
    character_name = serializers.CharField(source='character.name', read_only=True)

    class Meta:
        model = CharacterCampaignState
        fields = ['id', 'character', 'character_name', 'character_class', 'level', 'experience', 'hit_points', 'armor_class']

class CampaignSerializer(serializers.ModelSerializer):
    npcs = NPCSerializer(many=True, read_only=True)
    quests = QuestSerializer(many=True, read_only=True)
    characters = CharacterCampaignStateSerializer(many=True, read_only=True, source='charactercampaignstate_set')

    class Meta:
        model = Campaign
        fields = ['id', 'title', 'description', 'creator', 'npcs', 'quests', 'characters', 'created_at', 'updated_at']
        read_only_fields = ['creator', 'created_at', 'updated_at']