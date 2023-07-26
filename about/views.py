from django.shortcuts import render
from property.models import Property, Place, Category
from blog.models import Post
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def home(request):
    places = Place.objects.all()
    categories = Category.objects.all()
    recent_posts = Post.objects.all()[:4]
    context = {
        "places" : places,
        "categories" : categories,
        "recent_posts" : recent_posts,
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


def category_filter(request, category):
    category = Category.objects.get(name = category)

    property = Property.objects.filter(category = category)

    context = {
        'property_list' : property,
        "category" : category
    }
    return render(request, 'about/home_search.html', context)