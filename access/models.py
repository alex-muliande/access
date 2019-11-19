from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

#from .sheet2 import form_responses, process_response

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





class KnowMoringa(models.Model):
    name =models.CharField(max_length=30)
    email = models.EmailField(default = 'email@gmail.com')

    def __str__(self):
        return self.name
    @classmethod
    def all_emails5(cls):
        list_emails5=[]
        mails= cls.objects.filter(is_sent=False).all()
        for mail in mails:
            list_emails5.append(mail.email)
        return list_emails5
