from django.shortcuts import render
from .sheet2 import interest_responses, firstapplication_response
from .models import interestModel
from django.db.models import Q
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponseRedirect,JsonResponse


# Create your views here.
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


def firststageaccepted(request):
    all = interestModel.objects.all()
    first = []
    for elem in all:
        points = 0
        if int(elem.age) > 18:
            points += 1
        else:
            points -= 10
        # Add other filters here
        if item.prop.lower() in ['yes', 'yep', 'ndio']:
            pass
        # check if success

    print('first.count')
    print('########################################')

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
