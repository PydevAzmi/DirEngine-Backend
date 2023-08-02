from django import forms
from .models import Book, Review

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["date_from", "date_to", "guests", "childerns"]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["content", "rate"]