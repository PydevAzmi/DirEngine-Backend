from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Profile, User

from .forms import RegisterationForm , UserEditForm, ProfileEditForm, PasswordChangeForm
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

def profile(request):
    user = User.objects.get(id = request.user.id)
    profile = Profile.objects.get(user = user)
    context ={
        "user" : user,
        "profile" : profile      
              }
    return render(request, "profile/profile.html",context )

def profile_edit(request):
    user = request.user
    profile =Profile.objects.get(user = user)
    user_form = UserEditForm( instance= user)
    profile_form = ProfileEditForm(instance = profile)
    if request.method == "POST":
        user_form = UserEditForm(request.POST, instance = user)
        profile_form = ProfileEditForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            account = profile_form.save(commit = False)
            account.user = user
            account.save()
            return redirect(reverse('accounts:profile'))
    context= {
        "form" : user_form,
        "profile_form" : profile_form
    }
    return render(request, "profile/profile_edit.html", context)

def password_change(request):
    password_form = PasswordChangeForm(user = request.user)
    if request.method == "POST":
        password_form = PasswordChangeForm(user = request.user, data=request.POST)
        if password_form.is_valid():
            password_form.save()
            return redirect(reverse('accounts:profile'))

    return render(request, "registration/password_change.html", {"form" : password_form})