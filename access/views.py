from django.http import HttpResponseRedirect,JsonResponse
from django.shortcuts import render
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
            cert_image = form.cleaned_data['cert_image']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            recipient = InitialForm(name = name, email = email,cert_image=cert_image)
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
    