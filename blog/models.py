from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from taggit.managers import TaggableManager
# Create your models here.

class Post(models.Model):
    title = models.CharField(_("title"), max_length=50)
    tags = TaggableManager()
    image = models.ImageField(_("image"), upload_to= "blog/posts/", height_field=None, width_field=None, max_length=None)
    author = models.ForeignKey(User, verbose_name=_("author"), related_name="post_author", on_delete=models.CASCADE)
    created_at = models.DateTimeField(_("created_at"), default= timezone.now )
    category = models.ForeignKey("Category", verbose_name=_("category"), related_name="post_category", on_delete=models.CASCADE)
    description = models.TextField(_("description"))
    #comment = models.ForeignKey("Comment", verbose_name=_("comment"), related_name="post_comments", on_delete=models.CASCADE)
    slug = models.CharField(_("slug"), max_length=50, null=True, blank=True)

    def save(self, *args, **kwargs ):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Post,self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"slug": self.slug})
    
    class Meta:
        ordering = ["created_at"]
    

class Comment(models.Model):
    pass


class Category(models.Model):
    name = models.CharField(_("name"), max_length=50)
    image = models.ImageField(_("image"), upload_to="blog/category/")

    def __str__(self):
        return self.name