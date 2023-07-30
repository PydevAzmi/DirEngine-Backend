from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Profile
from .forms import RegisterationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate , login
# Create your views here.

def signup(request):
    signup_form = RegisterationForm
    if request.method == "POST":
        signup_form = RegisterationForm(data=request.POST)
        if signup_form.is_valid():
            signup_form.save()
            
            username = signup_form.cleaned_data['username']
            password = signup_form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect(reverse('accounts:profile'))

    return render(request, "registration/signup.html", {"form" : signup_form})