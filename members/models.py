from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

YEAR_CHOICES = [
    ('1', 'First'),
    ('2', 'Second'),
    ('3', 'Pre-Final'),
    ('4', 'Final'),
    ('5', 'Alumni'),
]

class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    year = models.CharField(choices=YEAR_CHOICES, max_length=6)
    github = models.CharField(max_length=100, null=True, blank=True)
    linkedin = models.CharField(max_length=100, null=True, blank=True)
    facebook = models.CharField(max_length=100, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    others = models.CharField(max_length=100, null=True, blank=True)
    profile_pic = models.ImageField(
        upload_to='member_profile_pic', default='default.jpg')
    slug = models.SlugField(unique=True, blank=True)
    first_password = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.first_name + '-' + self.user.last_name)
        slug_eixts = Member.objects.filter(slug=self.slug).exists()
        if slug_eixts:
            self.slug += '-' + str(self.user.id)
        super(Member, self).save(*args, **kwargs)

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other')
]


class Event(models.Model):
    name = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField()
    poster = models.ImageField(upload_to='EventPosters', default='DefaultEventPoster.jpg')
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    registration_start_date = models.DateField(null=True, blank=True)
    registration_end_date = models.DateField(null=True, blank=True)



class EventRegistration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, blank=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    year = models.CharField(max_length=15)
    branch = models.CharField(max_length=100)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=8)
    whatsapp_no = models.CharField(max_length=15)
    expectations = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstname 

class Contactus(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=150)
    msg = models.TextField()
    

    def __str__(self):
        return self.name

class Newsletter(models.Model):
    email = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,max_length=100)
    
    def __str__(self):
        return self.email



