from django.shortcuts import render,redirect
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
    form_data=interest_responses()
    response = firstapplication_response()

    # first=interestModel.objects.filter(commitment__icontains="yes",fluency__icontains="yes",computer_literacy__icontains="yes",residence__icontains="yes",residence_other__icontains="yes",age__gte=18).all()

    first=interestModel.objects.filter(commitment__icontains="yes",fluency__icontains="yes",computer_literacy__icontains="yes",age__gte=18).filter(Q(residence__icontains="yes")|Q(residence__icontains="I reside in Nairobi or within daily traveling distance of Nairobi")).all( )

    for email in  interestModel.objects.values_list('email', flat=True).distinct():
        interestModel.objects.filter(pk__in= interestModel.objects.filter(email=email).values_list('id', flat=True)[1:]).delete()
    
    return render(request,'interestaccepted.html',{'data':first})

 
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
    # mail1 = mail.EmailMessage('Final Test  ','Finall Email','moringaschoolaccess@gmail.com', receiver_list,connection = connection)
    send_this = EmailMultiAlternatives('subject','text_content','moringaschoolaccess@gmail.com',[email])    
    send_this.attach_alternative(html_content,'text/html')
    send_this.send()

def congragulate2(request):
    users_emails2=interestModel.all_emails2()
    print('Passed *********************** ',users_emails2)
    if users_emails2:
        for email_2 in users_emails2:
            user = interestModel.objects.filter(email = email_2).first()
            send_bulk2(user.email,user.name)
            if user:
                user.is_sent = True 
                user.save()
                # print('Passed *********************** ',email_2)
            else:
                # print('failed *********************** ',email_2)
                pass
        return JsonResponse({'sent':users_emails2})
    return JsonResponse({'sent':'upto date'})


