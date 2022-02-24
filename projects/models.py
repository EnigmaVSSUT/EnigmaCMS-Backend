from django.db import models
from members.models import Member
from django_mysql.models import ListCharField
from django.utils import timezone
from django.template.defaultfilters import slugify
from autoslug import AutoSlugField
from django.utils import timezone
import datetime
from django.contrib.auth.models import User
# Create your models here.
PROJECT_STATUS=[
    ('Ongoing','Ongoing'),
    ('Completed','Completed'),
    ('Stopped','Stopped')
]

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    project_link = models.TextField(null=True, blank=True)
    repository_link = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='project_pics', default='default_project.jpg')
    slug = models.SlugField(max_length=100, null=True, blank=True, unique=True)
    related_documents=models.ForeignKey('Document',null=True,on_delete=models.CASCADE,related_name="Project_Document")
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(null=True, blank=True)
    members = models.ManyToManyField(Member)
    domain_of_project=models.ManyToManyField('courses.Domain',related_name='Domain_of_Projects',blank=True)
    documents_of_project=models.ManyToManyField('Document',related_name='Project_related_docs',blank=True)
    tech_stack = ListCharField(
        base_field=models.CharField(max_length=40),
        size=20,
        null=True,
        max_length=(21 * 50)  # 6 * 10 character nominals, plus commas
    )
    is_Team = models.BooleanField(default=True, blank=True)
    contributor=models.ManyToManyField(Member,related_name='Project_contributors',blank=True)
    project_status=models.CharField(choices=PROJECT_STATUS,max_length=20,null=True,default='Ongoing')

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        slug_eixts = Project.objects.filter(slug=self.slug).exists()
        if slug_eixts:
            num = Project.objects.filter(name=self.name).count()
            self.slug += '-' + str(num + 1)
        super(Project, self).save(*args, **kwargs)


VISIBILITY_CHOICES=[
    ('PRIVATE','Private'),
    ('PUBLIC','Public'),
    ('ONLY-MEMBERS','Only-Members')
]
class Document(models.Model):
    title=models.CharField(max_length=50,blank=True,null=True)
    created_by=models.ManyToManyField(Member,blank=True,related_name="Document_Creators")
    visibility=models.CharField(choices=VISIBILITY_CHOICES,max_length=20,blank=True,null=True)
    visible_to=models.ManyToManyField(User,blank=True,related_name="Visible_To")
    time_stamp=models.DateTimeField(null=True, blank=True)
    project=models.ForeignKey(Project,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.title 

    def save(self, *args, **kwargs):
        if not self.time_stamp:
            self.time_stamp = timezone.now()
        super(Document, self).save(*args, **kwargs)
