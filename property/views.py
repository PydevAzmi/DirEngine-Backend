from django.shortcuts import render 
from django.urls import reverse
from .filter import PropertyFilter
from django.views.generic.edit import FormMixin
from django.views.generic import DetailView, ListView, FormView
from .forms import BookForm
from .models import Book, Review, Category, Place, PropertyImages, Property
from . import models
# Create your views here.


class FilteredListView(ListView):
    filterset_class = None
    def get_queryset(self):
        # Get the queryset however you usually would.  For example:
        queryset = super().get_queryset()
        # Then use the query parameters and the queryset to
        # instantiate a filterset and save it as an attribute
        # on the view instance for later.
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        # Return the filtered queryset
        return self.filterset.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the filterset to the template - it provides the form.
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
        if check_form.is_valid():
            myform = check_form.save(commit=False)
            myform.property = property
            myform.user = request.user
            myform.save()
    else:
        check_form = BookForm()

    context = {
        "property": property,
        "form" : check_form,
    }
    return render(request, template , context)