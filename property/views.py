from django.shortcuts import render
from .models import Book, Review, Category, Place, PropertyImages, Property
from django.views.generic import ListView, DetailView
# Create your views here.

class PropertyList(ListView):
    model = Property

class PropertyDetail(DetailView):
    pass

