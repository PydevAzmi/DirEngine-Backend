from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Company(models.Model):
    name = models.CharField(_("name"), max_length=50)
    desc = models.TextField(_("Description"), null=True , blank=True, max_length= 500 )
    email = models.EmailField(_("email"), max_length=254)
    logo = models.ImageField(_("logo"), upload_to="company/logo")
    call_us = models.CharField(_("Call_Us"), max_length=25)
    fb_link = models.URLField(_("Facebook"), max_length=200 ,null=True ,blank=True)
    insta_link = models.URLField(_("Instagram"), max_length=200 ,null=True ,blank=True)
    linkedin_link = models.URLField(_("Linkedin"), max_length=200 ,null=True ,blank=True)
    twit_link = models.URLField(_("Twitter"), max_length=200 ,null=True ,blank=True)
    emails = models.TextField(_("Emails") , max_length=100 ,null=True ,blank=True)
    numbers = models.TextField(_("Numbers"), max_length=100 ,null=True ,blank=True)
    address = models.TextField(_("Address") , max_length=100 ,null=True ,blank=True)
