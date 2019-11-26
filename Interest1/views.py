from django.shortcuts import render
from .sheet2 import interest_responses, firstapplication_response
from .models import interestModel
from django.db.models import Q


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

 