from typing import Iterable, Optional
from django.urls import reverse
from django.utils import timezone
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
# Based On The DirEngine Template the Models will be Created

COUNT= {
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
}

class Property(models.Model):
    name = models.CharField(_("name"), max_length=50)
    title = models.CharField(_("title"), max_length=50, null=True, blank=True)
    image = models.ImageField(_("main_image"), upload_to="property/images")
    price = models.IntegerField(_("price"),default=0)
    descritpion = models.TextField(_("descritpion"))
    place = models.ForeignKey("Place", verbose_name=_("places"),related_name= 'property_places', on_delete=models.CASCADE)
    category = models.ForeignKey("Category", verbose_name=_("category"), related_name="property_category", on_delete=models.CASCADE)
    created_at = models.DateTimeField(_("created_at"), default= timezone.now )
    slug = models.CharField(_("slug"), max_length=50, null=True, blank=True)

    def save(self, *args, **kwargs ):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Property,self).save(*args, **kwargs)
        
    def __str__(self):
        return self.name
    
    def get_related (self):
        related = Property.objects.filter(place = self.place)[:3]
        return(related)

    def get_absolute_url(self):
        return reverse("property:property_detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["price"]

class PropertyImages(models.Model):
    property = models.ForeignKey(Property, verbose_name=_("property"),related_name="property_images", on_delete=models.CASCADE)
    image = models.ImageField(_("image"), upload_to="property/images")

    def __str__(self):
        return str(self.property)

class Place(models.Model) :
    name = models.CharField(_("name"), max_length=50)
    image = models.ImageField(_("image"), upload_to="place/images")

    def __str__(self):
        return str(self.name)


class Category(models.Model):
    name = models.CharField(_("name"), max_length=50)
    image = models.ImageField(_("image"), upload_to="category/images")

    def __str__(self):
        return str(self.name)
    

class Review(models.Model):
    property = models.ForeignKey(Property, verbose_name=_("property"), related_name="property_Reviews", on_delete=models.CASCADE)
    rate = models.IntegerField(_("rate"), default=0)
    content = models.CharField(_("content"), max_length=150)
    created_at = models.DateTimeField(_("created_at"), default= timezone.now )
    author = models.ForeignKey(User, verbose_name=_("author"), related_name="review_author", on_delete=models.CASCADE)

    def __str__(self):
        return f'{str(self.property)} Review by {str(self.author)}'


class Book(models.Model):
    owner = models.ForeignKey(User, verbose_name=_("owner"), related_name="property_owner", on_delete=models.CASCADE)
    created_at = models.DateTimeField(_("created_at"),  default= timezone.now)
    property = models.ForeignKey(Property, verbose_name=_("property"), related_name="property_booked", on_delete=models.CASCADE)
    date_from = models.DateField(_("booked from"), default= timezone.now)
    date_to = models.DateField(_("booked to"), default= timezone.now)
    guests = models.IntegerField(_("guests"), choices=COUNT)
    childerns = models.IntegerField(_("childerns"), choices=COUNT)

    def __str__(self):
        return f'{str(self.property)} Booked by {str(self.owner)}'


