from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
# Based On The DirEngine Template the Models will be Created

class Property(models.Model):
    name = models.CharField(_("name"), max_length=50)
    image = models.ImageField(_("main_image"), upload_to="property/images")
    price = models.IntegerField(_("price"),default=0)
    descritpion = models.TextField(_("descritpion"))
    place = models.ForeignKey("Place", verbose_name=_("places"),related_name= 'property_places', on_delete=models.CASCADE)
    category = models.ForeignKey("Category", verbose_name=_("category"), related_name="proerty_category", on_delete=models.CASCADE)
    created_at = models.DateTimeField(_("created_at"), default= timezone.now )

    def __str__(self):
        return self.name

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
        return str(self.property)

class Book(models.Model):
    pass


class RelatedRooms(models.Model):
    pass