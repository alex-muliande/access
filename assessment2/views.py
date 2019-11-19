from django.shortcuts import render
from .sheet3 import assesment_responses, score_response
from .models import scoreModel


def scorecard(request):
    '''
    Assuming we make the api call
        
    '''
    # form_data=assesment_responses()
    # form_data=assesment_responses()
    # response = score_response()

    for email in  scoreModel.objects.values_list('email', flat=True).distinct():
        scoreModel.objects.filter(pk__in= scoreModel.objects.filter(email=email).values_list('id', flat=True)[1:]).delete()

    res= scoreModel.objects.all()
    return render(request,'scores.html',{'data':res})

    
def failed(request):
    # form_data=assesment_responses()
    # response = score_response()
    
    failed=scoreModel.objects.filter(status='Rejected').all()
    passed = scoreModel.objects.filter(status='Accepted').all()
   
    print(failed)
    # for f in failed:
        # scoreModel.objects.create(name=f.name,email=f.email,score=f.score,number=f.number,assesment_time=f.assesment_time)
        # for email in  scoreModel.objects.values_list('email', flat=True).distinct():
        #     scoreModel.objects.filter(pk__in= scoreModel.objects.filter(email=email).values_list('id', flat=True)[1:]).delete()


    return render(request,'rejected.html',{'failed':failed})


