from django.contrib import admin
from .models import About, FAQ, Subscribtion
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
class AboutAdmin(SummernoteModelAdmin):
    summernote_fields = ['our_goal', 'what_we_do', 'who_we_are']

admin.site.register(About)
admin.site.register(FAQ)
admin.site.register(Subscribtion)
