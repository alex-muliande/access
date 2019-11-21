from django.shortcuts import render
from .sheet2 import interest_responses, firstapplication_response
from .models import interestModel


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