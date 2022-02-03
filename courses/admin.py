from django.contrib import admin

# Register your models here.
from .models import Tag, Article, Track

admin.site.register(Tag)
admin.site.register(Article)
admin.site.register(Track)
