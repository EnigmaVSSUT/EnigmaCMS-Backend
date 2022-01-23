from django.db import models
from members.models import Member
from django_mysql.models import ListCharField
from django.utils import timezone
from django.template.defaultfilters import slugify
from autoslug import AutoSlugField

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    project_link = models.TextField(null=True, blank=True)
    repository_link = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='project_pics', default='default_project.jpg')
    slug = models.SlugField(max_length=100, null=True, blank=True, unique=True)

    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(null=True, blank=True)
    members = models.ManyToManyField(Member)
    tech_stack = ListCharField(
        base_field=models.CharField(max_length=40),
        size=20,
        null=True,
        max_length=(21 * 50)  # 6 * 10 character nominals, plus commas
    )

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        slug_eixts = Project.objects.filter(slug=self.slug).exists()
        if slug_eixts:
            num = Project.objects.filter(name=self.name).count()
            self.slug += '-' + str(num + 1)
        super(Project, self).save(*args, **kwargs)

