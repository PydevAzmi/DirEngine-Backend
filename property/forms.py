from django import forms
from .models import Book, Review, timezone

class DateInput(forms.DateInput):
    input_type = 'date'
    format=('%d/%m/%Y')

class BookForm(forms.ModelForm):
    def clean(self):
        now = timezone.now().date()
        start_date = self.cleaned_data.get('date_from')
        end_date = self.cleaned_data.get('date_to')
        if now > start_date:
            raise forms.ValidationError("start date must be later than or equal today" )
        elif end_date <= start_date:
            raise forms.ValidationError("End date must be later than start date")
        return self.cleaned_data
    
    class Meta:
        model = Book
        fields = ["date_from", "date_to", "guests", "childerns"]
        widgets = {
            'date_from': DateInput(),
            'date_to': DateInput(),
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["content", "rate"]