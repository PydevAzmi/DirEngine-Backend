from django import forms

class SendEmailForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    content = forms.CharField(widget=forms.Textarea, required=True)