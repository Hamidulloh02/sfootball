from rest_framework import serializers
from .models import AddStadium,Img,Time,Booking,Weeks
class ImgSerializers(serializers.ModelSerializer):
    class Meta:
        model = Img
        fields = ('id','images')
class TimeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = ('time','status')
class AddStadiumSerializers(serializers.ModelSerializer):
    fullimg = ImgSerializers(many = True)
    clock = TimeSerializers(many=True)
    author = serializers.CharField(source='author.username', read_only=True)
    region = serializers.CharField(source='region.name', read_only=True)
    class Meta:
        model = AddStadium
        fields = ('id','region', 'name', 'fullimg', 'number', 'card_number', 'card_name', 'location', 'clock', 'author')
        
class BookingSerializers(serializers.ModelSerializer):

    # stadium_clock = serializers.SerializerMethodField()s

    class Meta:
        model = Booking
        fields = '__all__'

    # def get_stadium_clock(self, obj):
    #     clock_qs = obj.stadium.clock.all()
    #     return TimeSerializers(clock_qs, many=True).data
class WeeksSerializers(serializers.ModelSerializer):
    class Meta:
        model = Weeks
        fields = ('id','name')