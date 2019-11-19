from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
#from .sheet2 import form_responses, process_response

class interestModel(models.Model):
    
    email=models.EmailField(max_length=250,default='Nan')
    your_name=models.CharField(max_length=50)
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
    is_sent = models.BooleanField(default=False)

    
    

    @classmethod
    def all_emails2(cls):
        list_emails2=[]
        mails= cls.objects.filter(is_sent=False).all()
        for mail in mails:
            list_emails2.append(mail.email)
        return list_emails2

class scoreModel(models.Model):
    Accepted = 'Accepted'
    Rejected = 'Rejected'
    Undecided = 'Undecided'

    STATUS= (Accepted,'Accepted'),(Rejected,'Rejected')
    name=models.CharField(max_length=250)
    email=models.EmailField(max_length=250)
    number=models.IntegerField()
    score=models.TextField(max_length=25)
    assesment_time=models.CharField(max_length=250)
    status=models.CharField(max_length=250,choices=STATUS, default='undecided')

    def save(self, *args, **kwargs):
        if not self.pk:
            print(self.score)
            l = self.score
            score, total = self.score.split('/')
            if int(score) > 11:
                self.status = 'Accepted'
            else:
                self.status = 'Rejected'
        super().save(*args, **kwargs)




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



class FormtwoResponses(models.Model):
    Pending = 'Pending'
    Accepted = 'Accepted'
    Rejected = 'Rejected'
    STATUS = (Pending, 'Pending'),(Accepted, 'Accepted'),(Rejected, 'Rejected')

    timestamp=models.CharField(max_length=250)
    all_names=models.CharField(max_length=250)
    email=models.CharField(max_length=250)
    currently_doing=models.CharField(max_length=250)
    work_experience=models.CharField(max_length=250) 
    work_experience_other=models.CharField(max_length=250)
    participated_job_project=models.CharField(max_length=250)
    run_a_business=models.CharField(max_length=250)
    career_goals=models.CharField(max_length=250)
    experience_in_tech=models.CharField(max_length=250)
    previous_experience=models.CharField(max_length=250)
    why_program=models.CharField(max_length=250)
    where_grow_up=models.CharField(max_length=250)
    live_most_year=models.CharField(max_length=250)
    currently_live=models.CharField(max_length=250)
    classify_neigbourhood=models.CharField(max_length=250)
    live_with=models.CharField(max_length=250)
    guardians=models.CharField(max_length=250)
    relationship_status=models.CharField(max_length=250)
    children=models.CharField(max_length=250)
    earnings_per_month=models.CharField(max_length=250)
    primary_financier=models.CharField(max_length=250)
    monthly_expenses=models.CharField(max_length=250)
    monthly_expenses_cost=models.CharField(max_length=250)
    support_others_financially=models.CharField(max_length=250)
    made_money_before=models.CharField(max_length=250)
    taken_bank_loan=models.CharField(max_length=250)
    who_took_loan=models.CharField(max_length=250)
    loan_value=models.CharField(max_length=250)
    loan_use=models.CharField(max_length=250)                        
    loan_collateral=models.CharField(max_length=250)
    gurdians_make_money=models.CharField(max_length=250)
    gurdians_employment=models.CharField(max_length=250)
    gurdians_earning=models.CharField(max_length=250)
    gurdians_support=models.CharField(max_length=250)
    names_age_supported=models.CharField(max_length=250)
    shool_and_schoolfees=models.CharField(max_length=250)
    spouse_make_money=models.CharField(max_length=250)
    spouse_employment_detail=models.CharField(max_length=250)
    spouse_earnings=models.CharField(max_length=250)
    smartphone_details=models.CharField(max_length=250)
    afford_smartphone=models.CharField(max_length=250)
    laptop_details=models.CharField(max_length=250)
    afford_laptop=models.CharField(max_length=250)
    guardians_car=models.CharField(max_length=250)
    form_of_transport=models.CharField(max_length=250)                          
    own_house=models.CharField(max_length=250)
    how_acquire_house=models.CharField(max_length=250)
    rent_cost=models.CharField(max_length=250)
    home_description=models.CharField(max_length=250)
    sent_home_schoolfees=models.CharField(max_length=250)
    time_out_of_school=models.CharField(max_length=250)
    schoolfees_per_term=models.CharField(max_length=250)
    high_school_financial_support=models.CharField(max_length=250)
    why_financial_support=models.CharField(max_length=250)
    why_dropout=models.CharField(max_length=250)
    university_name=models.CharField(max_length=250)
    university_fees=models.CharField(max_length=250)
    how_afford_fees=models.CharField(max_length=250)
    financial_support_university=models.CharField(max_length=250)
    who_howmuch_support_university=models.CharField(max_length=250)
    story_of_your_life=models.CharField(max_length=250)
    medium_complete_application=models.CharField(max_length=250)
    timetaken_complete_application=models.CharField(max_length=250)
    status=models.CharField(max_length=30, choices=STATUS, default=Pending)
    is_sent = models.BooleanField(default=False)

    @classmethod
    def all_emails3(cls):
        list_emails3=[]
        mails= cls.objects.filter(is_sent=False).all()
        for mail in mails:
            list_emails3.append(mail.email)
        return list_emails3
