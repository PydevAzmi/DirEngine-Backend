from django.contrib import admin
from .models import Book, Review, Category, Place, PropertyImages, Property
# Register your models here.
admin.site.register(Property)
admin.site.register(PropertyImages)
admin.site.register(Book)
admin.site.register(Review)
admin.site.register(Category)
admin.site.register(Place)
