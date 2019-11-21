from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import RegisterForm
    
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(response,f'Account created for {username}!')
            return redirect ('login')
    else:
        form= RegisterForm()
    return render (response,'registration/signup.html', {'form':form})

            

           
    #     return redirect("login")

    # else:
    #     form = RegisterForm()
    # return render (response, "registration/signup.html", {"form":form})

    