from django.shortcuts import render
from .sheet3 import assesment_responses, score_response
from .models import scoreModel



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