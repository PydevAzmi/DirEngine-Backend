from django.urls import path
from . import views
app_name = 'about'

urlpatterns = [
    path('', views.home, name = "home"),
    path('search/', views.home_search, name = "home_search")
]
