from django import forms 
from django.contrib.auth.forms import UserCreationForm


class RegisterationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ( "email",)