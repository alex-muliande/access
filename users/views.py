from django.shortcuts import render, redirect
from .forms import RegisterForm



def index(request):
    return render(request, 'index.html')

def register(response):
    if response.method == "POST":
        form = RegisterForm()
        if form.is_valid():
            form.save()
        return redirect("index")
        
    else:
        form = RegisterForm()
    return render (response, "registration/signup.html", {"form":form})

    