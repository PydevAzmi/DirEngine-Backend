from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
# Create your models here.
class About(models.Model):
    name = models.CharField(_("name"), max_length=50)
    who_we_are = models.TextField(_("who we are?"))
    what_we_do = models.TextField(_("what we do?"))
    our_goal = models.TextField(_("our goal"))
    image = models.ImageField(_("image"), upload_to="about/images")

    def __str__(self):
        return self.name

class FAQ (models.Model):
    question = models.CharField(_("question"), max_length=500)
    answer = models.TextField(_("answer"))

    def __str__(self):
        return self.question


class Subscribtion (models.Model):
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)
    email = models.EmailField(_("email"), max_length=254)
    created_at = models.DateField(_("created at"),default=timezone.now)

    class Meta:
        verbose_name = _("Subscribtion")
        verbose_name_plural = _("Subscribers")

    def __str__(self):
        return str(self.user)
