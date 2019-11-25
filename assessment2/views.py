from django.shortcuts import render,redirect
from .sheet3 import assesment_responses, score_response
from .models import scoreModel
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponseRedirect,JsonResponse



def scorecard(request):
    '''
    Assuming we make the api call
        
    '''
    form_data=assesment_responses()
    form_data=assesment_responses()
    response = score_response()

    for email in  scoreModel.objects.values_list('email', flat=True).distinct():
        scoreModel.objects.filter(pk__in= scoreModel.objects.filter(email=email).values_list('id', flat=True)[1:]).delete()

    res= scoreModel.objects.all()
    return render(request,'scores.html',{'data':res})

    

def accepted(request):
    # form_data=assesment_responses()
    # response = score_response()
    passed = scoreModel.objects.filter(status='Accepted').all()
    failed=scoreModel.objects.filter(status='Rejected').all()

    for f in failed:
        for email in  scoreModel.objects.values_list('email', flat=True).distinct():
            scoreModel.objects.filter(pk__in= scoreModel.objects.filter(email=email).values_list('id', flat=True)[1:]).delete()

    for f in passed:
        for email in  scoreModel.objects.values_list('email', flat=True).distinct():
            scoreModel.objects.filter(pk__in= scoreModel.objects.filter(email=email).values_list('id', flat=True)[1:]).delete()
    return render(request,'accepted.html',{'passed':passed, 'failed':failed})
    
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
            user = scoreModel.objects.filter(email = email_4).first()
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
