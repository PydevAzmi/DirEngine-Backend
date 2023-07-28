from django.urls import path
from . import views
app_name = 'about'

urlpatterns = [
    path('', views.home, name = "home"),
    path('search/', views.home_search, name = "home_search"),
    path('category/<str:category>', views.category_filter, name = "category_filter"),
    path("about/", views.AboutList.as_view(), name = "about")
]
