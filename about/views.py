from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from django.conf import settings
from property.models import Property, Place, Category
from .models import FAQ, About
from .forms import SendEmailForm
from blog.models import Post
from django.contrib.auth.models import User
from django.db.models import Q, Count
from django.views.generic import ListView
# Create your views here.


def home(request):
    places = Place.objects.all()
    categories = Category.objects.all()[:8]

    restaurants = Property.objects.filter(category__name__icontains = 'Restaurant' )[:5]
    hotels = Property.objects.filter(category__name__icontains = 'Hotel' )[:4]
    recent_posts = Post.objects.all()[:4]
    feature_places = Place.objects.all().annotate(listing = Count('property_places'))[:5]

    hotel_counter = Property.objects.filter(category__name__icontains = 'Hotel' ).count()
    restaurant_counter = Property.objects.filter(category__name__icontains = 'Restaurant' ).count()
    place_counter = Place.objects.all().count
    user_counter = User.objects.all().count()

    context = {
        "places" : places,
        "categories" : categories,

        "popular_restaurants" : restaurants,
        "popular_hotels" : hotels,
        "recent_posts" : recent_posts,
        "feature_places" : feature_places,
        
        'hotel_counter' : hotel_counter,
        'restaurant_counter' : restaurant_counter,
        'place_counter' : place_counter,
        'user_counter' : user_counter,
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

class AboutList(ListView):
    model = FAQ
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about"] = About.objects.last()
        return context
    
def tour(request):
    tours = Property.objects.filter(category__name__icontains = 'Tour' )[:4]
    
    context = {
        'property_list' : tours,
        "category" : "tour"
    }
    return render(request, "about/home_search.html", context)
    

def contact_us(request):
    form = SendEmailForm()
    if request.method == "POST":
        form = SendEmailForm(data=request.POST)
        if form.is_valid():
            print('valid')
            email = request.POST["email"]
            name = request.POST["name"]
            subject = request.POST["subject"]
            content = request.POST["content"]
            send_mail(
                subject= subject ,
                message=f"{content}\nFrom {name}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email])
            return redirect("contact/success/")
    else:
        form = SendEmailForm()

    return render(request, "about/contact.html", {'form' : form})

def success(request):
    return render(request,'about/success.html' )