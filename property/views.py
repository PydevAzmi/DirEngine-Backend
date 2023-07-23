from django.shortcuts import render
from .models import Book, Review, Category, Place, PropertyImages, Property
from django.views.generic import ListView, DetailView
# Create your views here.

class PropertyList(ListView):
    model = Property
    paginate_by = 15


class PropertyDetail(DetailView):
    DetailView.model = Property

