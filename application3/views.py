from django.shortcuts import render,redirect
from .models import FormtwoResponses
from .sheet1 import form_responses, process_response
import json
from django.http import HttpResponseRedirect,JsonResponse
from Interest1.models import interestModel
from django.core.mail import EmailMultiAlternatives


def myforms(request):
    '''
    assuming we make the api call
    '''
 

    # form_data=form_responses()
    # response = process_response()

    for email in  FormtwoResponses.objects.values_list('email', flat=True).distinct():
        FormtwoResponses.objects.filter(pk__in= FormtwoResponses.objects.filter(email=email).values_list('id', flat=True)[1:]).delete()


    res= FormtwoResponses.objects.all()

    pending = FormtwoResponses.objects.filter(status='Pending')
    accepted = FormtwoResponses.objects.filter(status='Accepted')
    rejected = FormtwoResponses.objects.filter(status='Rejected')

    params = {
        'pending':pending,
        'accepted':accepted,
        'rejected':rejected,
        'data':res,
    }
    return render(request,'results.html',params)
    
    # path('forms/', views.myforms, name ='forms'),

def FinalList(request):
     
    pending = FormtwoResponses.objects.filter(status='Pending')
    accepted = FormtwoResponses.objects.filter(status='Accepted')
    rejected = FormtwoResponses.objects.filter(status='Rejected')

    params = {
        'pending':pending,
        'accepted':accepted,
        'rejected':rejected,
    }

    # path('final/',views.FinalList),

    return render(request, 'final.html', params)




def StageOne(request):
    if 'pk' in request.GET and request.GET['pk']:
        pk = request.GET['pk']
        from .serializer import MyData

        application = FormtwoResponses.objects.get(pk=int(pk))
        # data2= MyData(application,many=False)
    
        # return JsonResponse(data2.data,safe=False)
        return render(request ,'fullform.html',{'app':application})
    return JsonResponse({'data':'No pk'})



def update_status(request,id):
    if request.method == 'GET':
        status = request.GET.get('status')
        form = FormtwoResponses.objects.get(pk = int(id))
        print('******* PENDING *******')
        if status == '-':
            print('******* PENDING *******')
            form.status='Pending'
            form.save()
        if status == '0':
            print('******* Rejected *******')
            form.status='Rejected'
            form.save()
        if status == '1':
            print('******* Accepted *******')  
            form.status='Accepted'
            form.save()
        return redirect(myforms)
         


def send_bulk3(email,name):
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
                print('Passed *********************** ',email_3)
            else:
                print('failed *********************** ',email_3)
                pass
        return JsonResponse({'sent':users_emails3})
    return JsonResponse({'sent':'upto date'})
    

    path('congrats3/',views.congragulate3)


