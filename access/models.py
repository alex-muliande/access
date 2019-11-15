from django.db import models
#from .sheet2 import form_responses, process_response

class interestModel(models.Model):
    
    email=models.EmailField(max_length=250,default='Nan')
    name=models.CharField(max_length=50)
    phone_number=models.CharField(max_length=250)
    guardians_number=models.TextField(max_length=250,default='Nan')
    age=models.TextField(max_length=250)
    date_of_birth=models.CharField(max_length=250)
    gender=models.TextField(max_length=250)
    prior_acceptance=models.TextField(max_length=250)
    highest_education_level=models.TextField(default='Nan',max_length=250)
    bachelors_degree=models.CharField(max_length=250,default='Nan' )
    completion_date=models.CharField(max_length=250)
    applied_to_uni=models.CharField(max_length=250)
    start_date=models.CharField(max_length=250)
    moringa_student=models.CharField(max_length=250)
    class_name=models.CharField(max_length=250)
    commitment=models.CharField(max_length=250)
    refered_by=models.CharField(max_length=250) 
    computer_literacy=models.CharField(max_length=250)   
    fluency=models.CharField(max_length=250)   
    residence=models.CharField(max_length=250)   
    residence_other=models.CharField(max_length=250)   
    residence_clarification=models.CharField(max_length=250)     

class scoreModel(models.Model):
    name=models.CharField(max_length=250)
    email=models.EmailField(max_length=250)
    number=models.IntegerField()
    score=models.TextField(max_length=25)
    assesment_time=models.CharField(max_length=250)
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
        return self.name

    @classmethod
    def all_emails(cls):
        list_emails=[]
        mails= cls.objects.filter(is_sent=False).all()
        for mail in mails:
            list_emails.append(mail.email)
        return list_emails


