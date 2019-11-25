from django.shortcuts import render, redirect
from .models import InitialForm, KnowMoringa
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import viewsets
from django.http import HttpResponseRedirect,JsonResponse
from .email import welcome_to_moringa,know_more
from django.views.generic import CreateView
from .forms import InitialformCreateView, MoreInformation
from django.core import mail
from django.http import HttpResponseRedirect,JsonResponse, HttpResponse, Http404
import json
from Interest1.models import interestModel
from django.http import HttpResponse
from django.core.mail import EmailMultiAlternatives

def send_bulk(email,name):

    html_content='''
<p>Hi,</p>
<br>
<p> To apply for our upcoming class, please click on this link <a href="https://forms.gle/nTS3pMi9d7owCUGw7">HERE</a> to fill out the initial application form. We will accept applicants on a first-come-first-serve basis.
 We can accept only a limited number of applications, so it is best to apply as soon as possible.
The latest date to submit this form is one week after today.
Before applying, note the eligibility requirements. To be considered for this scholarship, you must:
Be 18-35 years old
Come from a needy background
Have graduated high school
Not have completed your bachelor's degree coursework in the last 2 years
Not currently be studying in university
Be able to commit to the program full-time (Monday-Friday 8:30am - 6:00pm) and live in Nairobi for 6 months
Have basic digital literacy skills
Be fully fluent in written and spoken English
To learn more about the program and the admissions process, please see Access Program Overview.
We hope you apply to join us!</p> <br>
<p>Sincerely,</p>
<br>
<p>The Moringa School Access Team</p>
    '''.format(name)
    send_this = EmailMultiAlternatives('subject','text_content','moringaschoolaccess@gmail.com',[email])    
    send_this.attach_alternative(html_content,'text/html')
    send_this.send()

def index(request):
    
    return render(request, 'index.html')

def initial(request):
    if request.method == 'POST':
        form = InitialformCreateView(request.POST, request.FILES)
        if form.is_valid():
            KCSE_certificate_image = form.cleaned_data['KCSE_certificate_image']
            your_name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = InitialForm(KCSE_certificate_image=KCSE_certificate_image,your_name = your_name, email = email)
            recipient.save()
            welcome_to_moringa(your_name,email)
            return redirect('index')
    else:
        form = InitialformCreateView()

    return render(request, 'initial.html',{'form':form})


def congragulate(request):
    users_emails=InitialForm.all_emails()
    # print('Passed *********************** ',users_emails)
    if users_emails:
        for email_1 in users_emails:
            user = InitialForm.objects.filter(email = email_1).first()
            send_bulk(user.email,user.your_name)
            if user:
                user.is_sent = True 
                user.save()
                # print('Passed *********************** ',email_1)
            else:
                # print('failed *********************** ',email_1)
                pass
        return JsonResponse({'sent':users_emails})
    return JsonResponse({'sent':'upto date'})


def KnowMore(request):
    if request.method == 'POST':
        form = MoreInformation(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            recipient = KnowMoringa(name = name, email = email)
            recipient.save()
            know_more(name,email)
            return redirect('index')

    else:
        form = MoreInformation()

    return render(request, 'more.html',{'form':form})
