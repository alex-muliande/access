from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegisterForm



def index (request):
    return render(request, 'index.html')


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
           
        return redirect("login")

    else:
        form = RegisterForm()
    return render (response, "registration/signup.html", {"form":form})

    