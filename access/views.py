from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from .email import welcome_to_moringa
from django.views.generic import CreateView
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
            rec                                  ipient.save()
            welcome_to_moringa(name,email)
            HttpResponseRedirect('index')
    else:
        form = InitialformCreateView()
    return render(request, 'initial.html',{'form':form})
            

