from django.urls import path
from . import views
app_name = 'about'

urlpatterns = [
    path('', views.home, name = "home"),
    path('search/', views.home_search, name = "home_search"),
    path('category/<str:category>', views.category_filter, name = "category_filter"),
    path('category/Tour', views.tour, name = "category_tour"),
    path("about/", views.AboutList.as_view(), name = "about"),
    path("tour/", views.tour, name ='tour'),
    path("contact/", views.contact_us, name= "contact"),
    path("contact/success/", views.success, name= "email-sucess"),
]
