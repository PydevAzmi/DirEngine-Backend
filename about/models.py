from django.db import models
from django.utils.translation import gettext as _

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
