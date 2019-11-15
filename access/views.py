from django.http import HttpResponseRedirect,JsonResponse
from django.shortcuts import render
from .email import welcome_to_moringa
from django.views.generic import CreateView
from .models import InitialForm, FormtwoResponses
from .sheet1 import form_responses, process_response
import json
def index(request):
    return render(request, 'index.html')

class InitialformCreateView(CreateView):
    model = InitialForm
    template_name = 'initial.html'  
    fields = ['cert_image', 'name']



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
    

