from django.shortcuts import render 
from django.urls import reverse
from .filter import PropertyFilter
from django.views.generic.edit import FormMixin
from django.views.generic import DetailView, ListView, FormView
from .forms import BookForm, ReviewForm
from .models import Book, Review, Category, Place, PropertyImages, Property
from . import models
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

    if request.method == 'POST':
        check_form = BookForm(request.POST)
        review_form = ReviewForm(request.POST)
        if check_form.is_valid():
            myform = check_form.save(commit=False)
            myform.property = property
            myform.user = request.user
            myform.save()
        elif review_form.is_valid():
            myform = review_form.save(commit=False)
            myform.property = property
            myform.author = request.user
            myform.save()
    else:
        check_form = BookForm()
        review_form = ReviewForm()

    context = {
        "property": property,
        "review_form" : review_form,
        "form" : check_form,
    }
    return render(request, template , context)
