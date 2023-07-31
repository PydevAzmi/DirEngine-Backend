from django import forms
from django.forms import ValidationError 
from .models import User, Profile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class RegisterationForm(UserCreationForm):

    def clean(self):
       email = self.cleaned_data.get('email')
       if User.objects.filter(email=email).exists():
            raise ValidationError("This Email is already exists with deffirent user")

       
       return self.cleaned_data
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ( "email",)



class UserEditForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email']

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']