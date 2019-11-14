from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegisterForm


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            
            f"('Your post has been created!', 'success')"

           
        return redirect("login")

    else:
        form = RegisterForm()
    return render (response, "registration/signup.html", {"form":form})

    