from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class InitialForm(models.Model):
    cert_image = models.ImageField(upload_to = 'media/images')
    name =models.CharField(max_length=30)
    date_posted = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(default = 'email@gmail.com')

    def __str__(self):
        return self.name



