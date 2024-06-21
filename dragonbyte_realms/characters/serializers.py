# characters/serializers.py

from rest_framework import serializers
from .models import Character, Skill, InventoryItem
from campaigns.models import CharacterCampaignState

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name', 'description']

class InventoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItem
        fields = ['id', 'name', 'description', 'quantity']

class CharacterCampaignStateSerializer(serializers.ModelSerializer):
    campaign_title = serializers.CharField(source='campaign.title', read_only=True)

    class Meta:
        model = CharacterCampaignState
        fields = ['id', 'campaign', 'campaign_title', 'character_class', 'level', 'experience', 'hit_points', 'armor_class']

class CharacterSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)
    inventory = InventoryItemSerializer(many=True, read_only=True)
    campaign_states = serializers.SerializerMethodField()

    class Meta:
        model = Character
        fields = ['id', 'name', 'race', 'user', 'strength', 'dexterity', 'constitution', 
                  'intelligence', 'wisdom', 'charisma', 'background', 'skills', 'inventory', 
                  'campaign_states', 'created_at', 'updated_at']
        read_only_fields = ['user', 'created_at', 'updated_at']

    def get_campaign_states(self, obj):
        states = CharacterCampaignState.objects.filter(character=obj)
        return CharacterCampaignStateSerializer(states, many=True).data
