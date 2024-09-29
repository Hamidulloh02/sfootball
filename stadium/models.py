from django.db import models
from django.contrib.auth.models import User

DAYS_OF_THE_WEEK = [
    ('Mon', 'Monday'),
    ('Tue', 'Tuesday'),
    ('Wed', 'Wednesday'),
    ('Thu', 'Thursday'),
    ('Fri', 'Friday'),
    ('Sat', 'Saturday'),
    ('Sun', 'Sunday'),
]
# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=500)
    def __str__(self):
        return self.name
    


class AddStadium(models.Model):
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=500)
    location = models.CharField(max_length=500)
    number = models.CharField(max_length=500)
    card_number = models.CharField(max_length=500)
    card_name = models.CharField(max_length=500)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Img(models.Model):
    images = models.ImageField(upload_to="./img")
    post = models.ForeignKey(AddStadium, on_delete=models.CASCADE,null=True, related_name='fullimg')


class Time(models.Model):
    time = models.CharField(max_length=11)
    status = models.BooleanField(default=False)
    post = models.ForeignKey(AddStadium, on_delete=models.CASCADE,null=True, related_name='clock')
    def __str__(self):
        return self.time


class Booking(models.Model):
    stadium = models.ForeignKey(AddStadium, on_delete=models.CASCADE)
    img = models.ImageField(upload_to="./img")
    day_of_week = models.CharField(max_length=3, choices=DAYS_OF_THE_WEEK)
    hour = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('stadium', 'day_of_week', 'hour')  

    def __str__(self):
        return f'{self.stadium.name} booked on {self.get_day_of_week_display()} at {self.hour}:00'

class Weeks(models.Model):
    name = models.CharField(max_length=500)
    stadium = models.ForeignKey(AddStadium, on_delete=models.CASCADE,null=True, related_name='stadium')
    def __str__(self):
        return self.name