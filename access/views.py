from django.shortcuts import render, redirect
from .models import *
from django.http import Http404
from django.contrib.auth.models import User
from rest_framework import viewsets
from .sheet2 import interest_responses, firstapplication_response
from .sheet3 import assesment_responses, score_response
# from django.contrib.auth.models import User
# from django.shortcuts import render
# from .filters import UserFilter

# Create your views here.
#class Profileview(viewsets.ModelViewSet):
    #queryset= Profile.objects.all()
    #serializer_class = ProfileSerializer


def homepage(request):
    '''
    assuming we make the api call
    
    '''
    
    form_data=interest_responses()
    response = firstapplication_response()

    for email in  interestModel.objects.values_list('email', flat=True).distinct():
        interestModel.objects.filter(pk__in= interestModel.objects.filter(email=email).values_list('id', flat=True)[1:]).delete()

    res= interestModel.objects.all()
    return render(request,'interest.html',{'data':res})

def scorecard(request):
    '''
    Assuming we make the api call
        
    '''
    # form_data=assesment_responses()
    form_data=assesment_responses()
    response = score_response()

    for email in  scoreModel.objects.values_list('email', flat=True).distinct():
        scoreModel.objects.filter(pk__in= scoreModel.objects.filter(email=email).values_list('id', flat=True)[1:]).delete()

    res= scoreModel.objects.all()
    return render(request,'scores.html',{'data':res})
    
def failed(request):
    # form_data=assesment_responses()
    response = score_response()
    
    failed=scoreModel.objects.filter(score__lte=11).all()
    print()
    print('failed')
    # for f in failed:
        # scoreModel.objects.create(name=f.name,email=f.email,score=f.score,number=f.number,assesment_time=f.assesment_time)
        # for email in  scoreModel.objects.values_list('email', flat=True).distinct():
        #     scoreModel.objects.filter(pk__in= scoreModel.objects.filter(email=email).values_list('id', flat=True)[1:]).delete()

    return render(request,'rejected.html',{'data':failed})

from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,JsonResponse
from .email import welcome_to_moringa
from django.views.generic import CreateView
from .models import InitialForm
from django.http import HttpResponse
from .forms import InitialformCreateView
from django.core import mail

def send_bulk(emails):
    connection = mail.get_connection()

    connection.open()
    receiver_list = emails
    mail1 = mail.EmailMessage('Final Test ','Finall Email','wachirabeatice2020@gmail.com', receiver_list,connection = connection)
    mail1.send()

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
            welcome_to_moringa(name,email)
            HttpResponseRedirect('index')
    else:
        form = InitialformCreateView()

    return render(request, 'initial.html',{'form':form})


def congragulate(request):
    users_emails=InitialForm.all_emails()
    print('Passed *********************** ',users_emails)
    if users_emails:
        send_bulk(users_emails)
        for email_1 in users_emails:
            user = InitialForm.objects.filter(email = email_1).first()
            if user:
                user.is_sent = True 
                user.save()
                print('Passed *********************** ',email_1)
            else:
                print('failed *********************** ',email_1)
                pass
        return JsonResponse({'sent':users_emails})
    return JsonResponse({'sent':'upto date'})
    
