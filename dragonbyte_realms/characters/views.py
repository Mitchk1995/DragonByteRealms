# characters/views.py

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Character, Skill, InventoryItem
from .serializers import CharacterSerializer, SkillSerializer, InventoryItemSerializer

class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = [IsAuthenticated]  # Enforce authentication

    def get_serializer_class(self):
        if self.action == 'create':
            return CharacterSerializer
        return CharacterSerializer

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)
        else:
            raise serializer.ValidationError("You must be logged in to create a character.")

    @action(detail=True, methods=['post'])
    def add_skill(self, request, pk=None):
        character = self.get_object()
        serializer = SkillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(character=character)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def add_inventory_item(self, request, pk=None):
        character = self.get_object()
        serializer = InventoryItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(character=character)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def level_up(self, request, pk=None):
        character = self.get_object()
        character.level += 1
        character.hit_points += 5  # This is a simple example. You might want to make this more complex based on class, etc.
        character.save()
        return Response({'message': f'{character.name} leveled up to level {character.level}!'}, status=status.HTTP_200_OK)
