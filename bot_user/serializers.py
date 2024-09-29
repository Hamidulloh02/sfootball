from rest_framework import serializers
from .models import NicUser


class NicUserSerializers(serializers.ModelSerializer):
  class Meta:
    model = NicUser
    fields = ('id', 'nicname')

        
