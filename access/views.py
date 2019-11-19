from django.shortcuts import render, redirect
from .models import InitialForm
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import viewsets
from .email import welcome_to_moringa
from django.views.generic import CreateView
from .forms import InitialformCreateView
from django.core import mail
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,JsonResponse, HttpResponse, Http404
from django.shortcuts import render,redirect
from .email import welcome_to_moringa
import json
from .models import InitialForm,KnowMoringa
from django.http import HttpResponse
from .forms import InitialformCreateView,MoreInformation
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
    # form_data=interest_responses()
    # response = firstapplication_response()

    for email in  interestModel.objects.values_list('email', flat=True).distinct():
        interestModel.objects.filter(pk__in= interestModel.objects.filter(email=email).values_list('id', flat=True)[1:]).delete()

    res= interestModel.objects.all()
    return render(request,'interest.html',{'data':res})




def send_bulk(email,name):
    # connection = EmailMultiAlternatives.get_connection()

    # connection.open()
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
    <p>Thank you for filling out the initial application form. We have confirmed you meet our basic eligibility criteria.
    The next step in the application process is our full application.
    You will be required to submit the full application one week after we send it to you.
    To proceed in the selection process, kindly click on this link to complete the application form. 
    <a href="https://forms.gle/PdtdEAtit4yPoKXTA">HERE</a>
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
    users_emails2=interestModel.all_emails2()
    print('Passed *********************** ',users_emails2)
    if users_emails2:
        for email_2 in users_emails2:
            user = interestModel.objects.filter(email = email_2).first()
            send_bulk2(user.email,user.your_name)
            if user:
                user.is_sent = True 
                user.save()
                # print('Passed *********************** ',email_2)
            else:
                # print('failed *********************** ',email_2)
                pass
        return JsonResponse({'sent':users_emails2})
    return JsonResponse({'sent':'upto date'})
###########################################
def send_bulk6(email,name):
    # connection = EmailMultiAlternatives.get_connection()

    # connection.open()
    html_content='''
    <p>Hello,</p>
    <br>
    <p>Hello,
    Thank you for your interest in the Moringa School Access Program.
    We have considered your request for this scholarship and regret to inform you that you do not meet our eligibility criteria. As a result, we will be unable to move you forward in the application process.
    We wish you the utmost success in your future endeavors.
    </p>
    <br>
    <p>Sincerely,</p>
    <br>
    <p>The Moringa School Access Team</p>
    '''.format(name)
    send_this = EmailMultiAlternatives('subject','text_content','wachirabeatice2020@gmail.com',[email])    
    send_this.attach_alternative(html_content,'text/html')
    send_this.send()

def rejected(request):
    users_emails6=interestModel.all_emails6()
    print('Passed *********************** ',users_emails6)
    if users_emails6:
        for email_6 in users_emails6:
            user = interestModel.objects.filter(email = email_6).first()
            send_bulk6(user.email,user.your_name)
            if user:
                user.is_sent = True 
                user.save()
                print('Passed *********************** ',email_6)
            else:
                print('failed *********************** ',email_6)
                pass
        return JsonResponse({'sent':users_emails6})
    return JsonResponse({'sent':'upto date'})
###########################################
def send_bulk3(email,name):
    html_content='''
    <p>Hi,</p>
    <br>
    <p>Thank you for completing the application form. Congratulations! You are proceeding to the next stage of the admissions process.
    For the next stage, kindly complete the following assessment by clicking on this link.<a href="https://forms.gle/87cDDKQnThyi423V9">HERE</a>
    It is meant to assess your skills in digital literacy.
    Please complete this by end of the day.
    If you pass, the final step is an interview at Moringa School.</p>
    <br>
    <p>Best wishes,</p>
    <br>
    <p>The Moringa School Access Team</p>
    '''.format(name)
    send_this = EmailMultiAlternatives('subject','text_content','wachirabeatice2020@gmail.com',[email])    
    send_this.attach_alternative(html_content,'text/html')
    send_this.send()

def congragulate3(request):
    users_emails3=FormtwoResponses.all_emails3()
    print('Passed *********************** ',users_emails3)
    if users_emails3:
        for email_3 in users_emails3:
            user = interestModel.objects.filter(email = email_3).first()
            send_bulk3(user.email,user.your_name)
            if user:
                user.is_sent = True 
                user.save()
                # print('Passed *********************** ',email_3)
            else:
                # print('failed *********************** ',email_3)
                pass
        return JsonResponse({'sent':users_emails3})
    return JsonResponse({'sent':'upto date'})

###########################################
def send_bulk4(email,name):
    # connection = EmailMultiAlternatives.get_connection()

    # connection.open()
    html_content='''
    <p>Hi,</p>
    <br>
    <p>Congratulations! We have reviewed your application and would like to invite you for an independent interview at Moringa School. This is the final phase of the application process.
    Your live interview has been scheduled on Friday this week the time will be communicated. Your interview will take 30 minutes. You must arrive on time. You are allowed only one interview slot, and if you arrive late, we will not be able to interview you.
    Please respond to this email confirming that you will attend the interview.
    Directions to Moringa School:
    - Here is a google maps link to our location.
    - If you are using matatu transport, kindly alight at Prestige Plaza along Ngong Road.
    Spot a signboard that reads "Double Tree by Hilton" and walk along the same road you see the sign post into Ngong Lane Plaza opposite Faulu Bank. Our offices are located on the first floor of Ngong Lane Plaza.
    See you on your interview day! 
    </p>
    <br>
    <p>Regards,</p>
    <br>
    <p>The Moringa School Access Team</p>
    '''.format(name)
    # receiver_list = emails
    # mail1 = mail.EmailMessage('Final Test  ','Finall Email','wachirabeatice2020@gmail.com', receiver_list,connection = connection)
    send_this = EmailMultiAlternatives('subject','text_content','wachirabeatice2020@gmail.com',[email])    
    send_this.attach_alternative(html_content,'text/html')
    send_this.send()

def congragulate4(request):
    users_emails4=scoreModel.all_emails4()
    print('Passed *********************** ',users_emails4)
    if users_emails4:
        for email_4 in users_emails4:
            user = interestModel.objects.filter(email = email_4).first()
            send_bulk4(user.email,user.your_name)
            if user:
                user.is_sent = True 
                user.save()
                print('Passed *********************** ',email_4)
            else:
                print('failed *********************** ',email_4)
                pass
        return JsonResponse({'sent':users_emails4})
    return JsonResponse({'sent':'upto date'})





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
    

###########################################
def send_bulk4(email,name):
    # connection = EmailMultiAlternatives.get_connection()

    # connection.open()
    html_content='''
    <p>Hi,</p>
    <br>
    <p>Congratulations! We have reviewed your application and would like to invite you for an independent interview at Moringa School. This is the final phase of the application process.
    Your live interview has been scheduled on Friday this week the time will be communicated. Your interview will take 30 minutes. You must arrive on time. You are allowed only one interview slot, and if you arrive late, we will not be able to interview you.
    Please respond to this email confirming that you will attend the interview.
    Directions to Moringa School:
    - Here is a google maps link to our location.
    - If you are using matatu transport, kindly alight at Prestige Plaza along Ngong Road.
    Spot a signboard that reads "Double Tree by Hilton" and walk along the same road you see the sign post into Ngong Lane Plaza opposite Faulu Bank. Our offices are located on the first floor of Ngong Lane Plaza.
    See you on your interview day! 
    </p>
    <br>
    <p>Regards,</p>
    <br>
    <p>The Moringa School Access Team</p>
    '''.format(name)
    # receiver_list = emails
    # mail1 = mail.EmailMessage('Final Test  ','Finall Email','wachirabeatice2020@gmail.com', receiver_list,connection = connection)
    send_this = EmailMultiAlternatives('subject','text_content','wachirabeatice2020@gmail.com',[email])    
    send_this.attach_alternative(html_content,'text/html')
    send_this.send()

def congragulate4(request):
    users_emails4=scoreModel.all_emails4()
    print('Passed *********************** ',users_emails4)
    if users_emails4:
        for email_4 in users_emails4:
            user = interestModel.objects.filter(email = email_4).first()
            send_bulk4(user.email,user.your_name)
            if user:
                user.is_sent = True 
                user.save()
                print('Passed *********************** ',email_4)
            else:
                print('failed *********************** ',email_4)
                pass
        return JsonResponse({'sent':users_emails4})
    return JsonResponse({'sent':'upto date'})

def KnowMore(request):
    if request.method == 'POST':
        form = MoreInformation(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            recipient = KnowMoringa(name = name, email = email)
            recipient.save()
            return redirect('index')
    else:
        form = MoreInformation()

    return render(request, 'more.html',{'form':form})

def more(email,name):

    html_content='''
    <p>Hi,</p>
    <br>
    <p>Moringa School is a world-class learning program which trains students to become software developers. We connect our students with employment opportunities after they graduate and teach them skills that will last a lifetime.
    Click here for a video about the Moringa experience.
    Click here for Moringa School’s website.
    The Access Program gives scholarships to youth from needy backgrounds. The scholarship value is 400,000 KES. To learn more about the program, click here: Access Program Overview.
    The admissions process is multi-stage. You must pass each stage to proceed. To learn more, read the section called "Admissions Process" in Access Program Overview.
    Contact admissions.access@moringaschool.com if you would like to apply or require more information!
    </p>
    <br>
    <p>Regards,</p>

    '''.format(name)
    # receiver_list = emails
    # mail1 = mail.EmailMessage('Final Test  ','Finall Email','wachirabeatice2020@gmail.com', receiver_list,connection = connection)
    send_this = EmailMultiAlternatives('subject','text_content','wachirabeatice2020@gmail.com',[email])    
    send_this.attach_alternative(html_content,'text/html')
    send_this.send()

def moreinfo(request):
    users_emails5=scoreModel.all_emails5()
    print('Passed *********************** ',users_emails5)
    if users_emails5:
        for email_5 in users_emails5:
            user = interestModel.objects.filter(email = email_5).first()
            send_bulk5(user.email,user.your_name)
            if user:
                user.is_sent = True 
                user.save()
                print('Passed *********************** ',email_5)
            else:
                print('failed *********************** ',email_5)
                pass
        return JsonResponse({'sent':users_emails5})
    return JsonResponse({'sent':'upto date'})
