from django.urls import path
from . import views

app_name = "property"

urlpatterns = [
    path('',views.PropertyList.as_view(), name = "property_list"),
    path('new',views.property_create, name = "add_property"),
    path('<slug:slug>',views.property_detail, name = "property_detail"),
]