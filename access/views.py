from django.http import HttpResponseRedirect
from django.shortcuts import render
from .email import welcome_to_moringa
from django.views.generic import CreateView
from .models import InitialForm

def index(request):
    return render(request, 'index.html')

class InitialformCreateView(CreateView):
    model = InitialForm
    template_name = 'initial.html'  
    fields = ['cert_image', 'name']

