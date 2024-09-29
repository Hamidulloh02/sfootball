from django.shortcuts import render
from .models import AddStadium,Booking
from .serializers import AddStadiumSerializers,BookingSerializers,WeeksSerializers
from rest_framework import permissions, generics
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

# Create your views here.

#import filter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

class StadiumAddView(generics.ListCreateAPIView):
    queryset = AddStadium.objects.all()
    serializer_class = AddStadiumSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return AddStadium.objects.all()
        # Foydalanuvchining o'z postlarini ko'rsatish
        return AddStadium.objects.filter(author=self.request.user)
class StadiumSingle(generics.RetrieveUpdateDestroyAPIView):
    queryset = AddStadium.objects.all().order_by('-id')
    serializer_class = AddStadiumSerializers
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        if self.request.user.is_superuser:
            return AddStadium.objects.all()
        # Foydalanuvchining o'z postlarini ko'rsatish
        return AddStadium.objects.filter(author=self.request.user)
class StadiumFilter(generics.ListAPIView):
    queryset = AddStadium.objects.all()
    serializer_class = AddStadiumSerializers
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['region', 'name']
    search_fields = ['region', 'name']

class BookingView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializers
    permission_classes = [IsAuthenticated]
    def create(self, request, *args, **kwargs):
        day_of_week = request.data.get('day_of_week')
        stadium_id = request.data.get('stadium')
        hour = request.data.get('hour')

        if Booking.objects.filter(stadium_id=stadium_id, day_of_week=day_of_week, hour=hour).exists():
            return Response({'error': 'This slot is already booked.'}, status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)

class WeeksView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = WeeksSerializers
    permission_classes = [IsAuthenticated]



