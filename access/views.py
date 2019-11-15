from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,JsonResponse
from .email import welcome_to_moringa
from django.views.generic import CreateView
from .models import InitialForm
from django.http import HttpResponse
from .forms import InitialformCreateView
from django.core.mail import EmailMultiAlternatives

def send_bulk(email,name):
    # connection = EmailMultiAlternatives.get_connection()

    # connection.open()
    html_content='''
    <h2>Initial Application Form Complete</h2>
    <p style="color: red;">(Accepted after Initial Application Form)</p>
    <br>
    <p>Dear Applicant ,</p>
    <br>
    <p>Thank you for filling out the initial application form. We have confirmed you meet our basic eligibility criteria. <br>
    The next step in the application process is our full application. Please click <a href="https://forms.gle/87cDDKQnThyi423V9">HERE</a>  You are required to submit the full application one week after we send it to you.
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

