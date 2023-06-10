from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserInfo(models.Model):
    nim = models.CharField(max_length=264)
    kelas = models.CharField(max_length=264)
    jurusan = models.CharField(max_length=264)
    foto = models.ImageField(blank=True, upload_to='images/')
    
    def __str__(self):
        return self.nim