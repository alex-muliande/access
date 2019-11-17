from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class InitialForm(models.Model):
    KCSE_certificate_image = models.ImageField(upload_to = 'media/images')
    your_name =models.CharField(max_length=30)
    date_posted = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(default = 'email@gmail.com')
    is_sent= models.BooleanField(default=False)

    def __str__(self):
        return self.your_name


    @classmethod
    def all_emails(cls):
        list_emails=[]
        mails= cls.objects.filter(is_sent=False).all()
        for mail in mails:
            list_emails.append(mail.email)
        return list_emails


