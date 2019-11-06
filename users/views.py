from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegisterForm


def register(response):
    if response.method == "POST":
        form = RegisterForm()
        if form.is_valid():
            form.save()
            username = form.cleaned_data('username')
            email = form.cleaned_data('email')
            password = form.cleaned_data('password1')
            user = authenticate(username=username,email=email,password=password)
        return redirect("login")

    else:
        form = RegisterForm()
    return render (response, "registration/signup.html", {"form":form})

    