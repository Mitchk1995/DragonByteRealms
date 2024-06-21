from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

class RegisterView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

@login_required
def profile_view(request):
    return render(request, 'user_auth/profile.html')