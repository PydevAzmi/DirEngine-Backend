from django.forms import ValidationError 
from .models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterationForm(UserCreationForm):

    def clean(self):
       email = self.cleaned_data.get('email')
       if User.objects.filter(email=email).exists():
            raise ValidationError("This Email is already exists with deffirent user")
       
       return self.cleaned_data
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ( "email",)