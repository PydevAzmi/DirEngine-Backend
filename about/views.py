from django.shortcuts import render
from property.models import Property, Place
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def home(request):
    places = Place.objects.all()

    context = {
        "places" : places
    }
    return render(request, 'about/home.html', context)


def home_search(request):
    name = request.GET.get('name')
    place = request.GET.get('place')

    property= Property.objects.filter(
        Q(name__icontains = name) &
        Q(place__name__icontains = place)
    )

    context = {
        'property_list' : property,
    }
    return render(request, 'about/home_search.html', context)