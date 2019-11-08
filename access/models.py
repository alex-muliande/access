from django.db import models
# from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class InitialForm(models.Model):
    cert_image = models.ImageField(upload_to = 'images')
    name =models.CharField(max_length=30)
    date_posted = models.DateTimeField(auto_now_add=True)


    def get_absolute_url(self):
        return reverse('index')


