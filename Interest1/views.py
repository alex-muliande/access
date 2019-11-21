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
    first=interestModel.objects.filter(Q(commitment__icontains="yes") & Q(fluency__icontains="yes") & Q(computer_literacy__icontains="yes") & Q(residence__icontains="yes")& Q(residencyothers__icontains="yes") & Q(age__gte=18))
    print('first.count')
    print('########################################')