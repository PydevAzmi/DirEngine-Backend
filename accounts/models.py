from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

def user_dir_path(instance, filename):
    return 'user/{0}/profile_photo/{1}'.format(instance.user, filename)

GENDER = [ 
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

class Profile(models.Model):
    user = models.ForeignKey(User, verbose_name=_("user"), related_name="user_profile", on_delete=models.CASCADE)
    profile_image = models.ImageField(_("profile_image"), upload_to=user_dir_path)
    gender = models.CharField(_("Gender"), max_length=10, choices=GENDER)
    country = CountryField(blank= True)

    def __str__(self):
        return str(self.user)
    
@receiver(post_save, sender=User)  
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)