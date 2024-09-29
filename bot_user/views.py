from django.shortcuts import render
from rest_framework import permissions, generics
from .models import NicUser
from .serializers import NicUserSerializers

# Create your views here.


class NicUserView(generics.ListCreateAPIView):
    queryset = NicUser.objects.all()
    serializer_class = NicUserSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
