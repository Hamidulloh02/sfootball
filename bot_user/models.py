from django.db import models

# Create your models here.

class NicUser(models.Model):
    nicname = models.CharField(max_length=500)

    def __srt__(self):
        return self.nicname