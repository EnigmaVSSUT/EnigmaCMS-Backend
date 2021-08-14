from django.contrib import admin
from . import models as member_models

admin.site.register(member_models.Member)