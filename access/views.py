from django.shortcuts import render, redirect
from .models import *
from django.http import Http404
from django.contrib.auth.models import User
from rest_framework import viewsets
from .sheet2 import interest_responses, firstapplication_response
from .sheet3 import assesment_responses, score_response
from django.http import HttpResponseRedirect,JsonResponse
from .email import welcome_to_moringa
from django.views.generic import CreateView
from .models import InitialForm
from django.http import HttpResponse
from .forms import InitialformCreateView
from django.core import mail
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,JsonResponse
from django.shortcuts import render,redirect
from .email import welcome_to_moringa
from django.views.generic import CreateView
from .models import InitialForm, FormtwoResponses
from .sheet1 import form_responses, process_response
import json
from .models import InitialForm
from django.http import HttpResponse
from .forms import InitialformCreateView
from django.core.mail import EmailMultiAlternatives

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
    
    failed=scoreModel.objects.filter(status='Rejected').all()
    passed = scoreModel.objects.filter(status='Accepted').all()
   
    print(failed)
    # for f in failed:
        # scoreModel.objects.create(name=f.name,email=f.email,score=f.score,number=f.number,assesment_time=f.assesment_time)
        # for email in  scoreModel.objects.values_list('email', flat=True).distinct():
        #     scoreModel.objects.filter(pk__in= scoreModel.objects.filter(email=email).values_list('id', flat=True)[1:]).delete()


    return render(request,'rejected.html',{'failed':failed})


def send_bulk(email,name):
    # connection = EmailMultiAlternatives.get_connection()

    # connection.open()
    html_content='''
  Hello,
Thank you for your interest in the Access Program! Our next class will start soon.  we will notify you when the application period for that class will open. Kindly send us an email that day and we will send you the link to apply.
Please review the requirements to confirm you qualify for the program before deciding to apply. To be considered for this scholarship, you must:
Be 18-35 years old
Come from a needy background
Have graduated high school
Not have completed your bachelor's degree coursework in the last 2 years
Not currently be studying in university
Have basic computer skills
Be fully fluent in both written and spoken English
Have a place to live in Nairobi
Be able to commit to the program full-time (Monday-Friday 8:30am - 6:00pm) for 6 months.
You can find more information about Moringa School and the Access Program below this email.
All the best,
The Access Program Team 

Moringa School is a world-class learning program which trains students to become software developers. We connect our students with employment opportunities after they graduate and teach them skills that will last a lifetime.
Click here for a video about the Moringa experience.
Click here for Moringa School’s website.
The Access Program gives scholarships to youth from needy backgrounds. The scholarship value is 400,000 KES. To learn more about the program, click here: Access Program Overview.
The admissions process is multi-stage. You must pass each stage to proceed. To learn more, read the section called "Admissions Process" in Access Program Overview.
    '''.format(name)
    # receiver_list = emails
    # mail1 = mail.EmailMessage('Final Test  ','Finall Email','wachirabeatice2020@gmail.com', receiver_list,connection = connection)
    send_this = EmailMultiAlternatives('subject','text_content','wachirabeatice2020@gmail.com',[email])    
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
            HttpResponseRedirect('index')
    else:
        form = InitialformCreateView()

    return render(request, 'initial.html',{'form':form})


def congragulate(request):
    users_emails=InitialForm.all_emails()
    print('Passed *********************** ',users_emails)
    if users_emails:
        for email_1 in users_emails:
            user = InitialForm.objects.filter(email = email_1).first()
            send_bulk(user.email,user.your_name)
            if user:
                user.is_sent = True 
                user.save()
                print('Passed *********************** ',email_1)
            else:
                print('failed *********************** ',email_1)
                pass
        return JsonResponse({'sent':users_emails})
    return JsonResponse({'sent':'upto date'})
###########################################
def send_bulk2(email,name):
    # connection = EmailMultiAlternatives.get_connection()

    # connection.open()
    html_content='''
    
    
    <h2>Application Form </h2>
    <p style="color: red;">(Launch of Application Form 2)</p>
    <br>
    <p>Hello,</p>
    <br>
    <p>We thank you for applying to the Moringa School Access Program.
    To proceed in the selection process, kindly click on this link to complete the application form. 
    <a href="https://forms.gle/87cDDKQnThyi423V9">HERE</a>
    If you qualify, the next step in the application process is an assessment. 
    
    Wishing you all the best!

    </p>
    <br>
    <p>Kind regards,</p>
    <br>
    <p>The Moringa School Access Team</p>
    '''.format(name)
    # receiver_list = emails
    # mail1 = mail.EmailMessage('Final Test  ','Finall Email','wachirabeatice2020@gmail.com', receiver_list,connection = connection)
    send_this = EmailMultiAlternatives('subject','text_content','wachirabeatice2020@gmail.com',[email])    
    send_this.attach_alternative(html_content,'text/html')
    send_this.send()

def congragulate2(request):
    users_emails2=interestModel.all_emails()
    print('Passed *********************** ',users_emails2)
    if users_emails2:
        for email_2 in users_emails2:
            user = interestModel.objects.filter(email = email_2).first()
            send_bulk2(user.email,user.your_name)
            if user:
                user.is_sent = True 
                user.save()
                print('Passed *********************** ',email_2)
            else:
                print('failed *********************** ',email_2)
                pass
        return JsonResponse({'sent':users_emails2})
    return JsonResponse({'sent':'upto date'})
###########################################
def send_bulk3(email,name):
    # connection = EmailMultiAlternatives.get_connection()

    # connection.open()
    html_content='''
    
    
    <h2>Application Form </h2>
    <p style="color: red;">(Launch of Application Form 2)</p>
    <br>
    <p>Hello,</p>
    <br>
    <p>We thank you for applying to the Moringa School Access Program.
    To proceed in the selection process, kindly click on this link to complete the application form. 
    <a href="https://forms.gle/87cDDKQnThyi423V9">HERE</a>
    If you qualify, the next step in the application process is an assessment. 
    
    Wishing you all the best!

    </p>
    <br>
    <p>Kind regards,</p>
    <br>
    <p>The Moringa School Access Team</p>
    '''.format(name)
    # receiver_list = emails
    # mail1 = mail.EmailMessage('Final Test  ','Finall Email','wachirabeatice2020@gmail.com', receiver_list,connection = connection)
    send_this = EmailMultiAlternatives('subject','text_content','wachirabeatice2020@gmail.com',[email])    
    send_this.attach_alternative(html_content,'text/html')
    send_this.send()

def congragulate3(request):
    users_emails3=interestModel.all_emails()
    print('Passed *********************** ',users_emails3)
    if users_emails3:
        for email_3 in users_emails3:
            user = interestModel.objects.filter(email = email_3).first()
            send_bulk3(user.email,user.your_name)
            if user:
                user.is_sent = True 
                user.save()
                print('Passed *********************** ',email_3)
            else:
                print('failed *********************** ',email_3)
                pass
        return JsonResponse({'sent':users_emails3})
    return JsonResponse({'sent':'upto date'})



def myforms(request):
    '''
    assuming we make the api call
    
    '''
    # form_data=form_responses()
    # form_data=form_responses()
    # response = process_response()

    for email in  FormtwoResponses.objects.values_list('email', flat=True).distinct():
        FormtwoResponses.objects.filter(pk__in= FormtwoResponses.objects.filter(email=email).values_list('id', flat=True)[1:]).delete()


    res= FormtwoResponses.objects.all()
    return render(request,'results.html',{'data':res})

def StageOne(request):
    if 'pk' in request.GET and request.GET['pk']:
        pk = request.GET['pk']
        from .serializer import MyData

        application = FormtwoResponses.objects.get(pk=int(pk))
        # data2= MyData(application,many=False)
    
        # return JsonResponse(data2.data,safe=False)
        return render(request ,'fullform.html',{'app':application})
    return JsonResponse({'data':'No pk'})



def FinalList(request):
     
    all = FormtwoResponses.objects.all()



    pending = FormtwoResponses.objects.filter(status='Pending')
    accepted = FormtwoResponses.objects.filter(status='Accepted')
    rejected = FormtwoResponses.objects.filter(status='Rejected')

    params = {
        'pending':pending,
        'accepted':accepted,
        'rejected':rejected,
    }

    return render(request, 'final.html', params)
    

