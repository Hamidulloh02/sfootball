from django.contrib import admin
from .models import AddStadium, Img,Region,Time,Booking,Weeks

class ImgInline(admin.TabularInline):
    model = Img
    extra = 1
class TimeInline(admin.TabularInline):
    model = Time
    extra = 0
class AddStadiumAdmin(admin.ModelAdmin):
    inlines = [ImgInline,TimeInline]

admin.site.register(AddStadium, AddStadiumAdmin)
# Register your models here.
admin.site.register(Region)
admin.site.register(Booking)
admin.site.register(Weeks)
