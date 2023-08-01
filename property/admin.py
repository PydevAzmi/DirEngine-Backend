from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Book, Review, Category, Place, PropertyImages, Property


# Register your models here.
class PropertyAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    list_display = ["name", "avg_rating"]


admin.site.register(Property,PropertyAdmin)
admin.site.register(PropertyImages)
admin.site.register(Book)
admin.site.register(Review)
admin.site.register(Category)
admin.site.register(Place)
