from django.shortcuts import render
from .email import welcome_to_moringa

# Create your views here.

def index(request):
    return render(request, 'index.html')