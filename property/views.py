from django.shortcuts import render 
from .filter import PropertyFilter
from django.utils import timezone
from django.contrib import messages
from django.views.generic.edit import FormMixin
from django.views.generic import DetailView, ListView, FormView
from .forms import BookForm, ReviewForm
from .models import Property

# Create your views here.


class FilteredListView(ListView):
    filterset_class = None
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        return self.filterset.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

class PropertyList(FilteredListView):
    model = Property
    paginate_by = 15
    filterset_class = PropertyFilter


def property_detail(request, slug):
    property = Property.objects.get(slug = slug)
    template = "property/property_detail.html"
    check_form = BookForm()
    review_form = ReviewForm()
    if request.method == 'POST':
        if "Availability" in request.POST:
            check_form = BookForm(request.POST)
            date_from = request.POST.get("date_from")
            if check_form.is_valid():
                date_from = check_form.cleaned_data["date_from"]
                date_to = check_form.cleaned_data["date_to"]
                myform = check_form.save(commit=False)
                is_avaliable = property.check_avilablity(date_from, date_to)
                if is_avaliable:
                    myform.property = property
                    myform.user = request.user
                    myform.save()
                    messages.success(request, "Avalible, Booked succesfully")
                else :
                    messages.warning(request, "Not Avaliable")

        elif "Review" in request.POST:
            review_form = ReviewForm(request.POST)
            if review_form.is_valid():
                myform = review_form.save(commit=False)
                myform.property = property
                myform.author = request.user
                myform.save()
                

    context = {
        "property": property,
        "review_form" : review_form,
        "avaliability_form" : check_form,
    }
    return render(request, template , context)
