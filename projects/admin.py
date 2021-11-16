from django.contrib import admin
from . import models as project_models
# Register your models here.

admin.site.register(project_models.Project)