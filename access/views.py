from django.http import HttpResponseRedirect,JsonResponse
from django.shortcuts import render
from .email import welcome_to_moringa
from django.views.generic import CreateView
from .models import InitialForm, FormtwoResponses
from .sheet1 import form_responses, process_response
import json
from .models import InitialForm
from django.http import HttpResponse
from .forms import InitialformCreateView
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
    

