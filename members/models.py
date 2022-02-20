from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django_mysql.models import ListCharField
from autoslug import AutoSlugField

YEAR_CHOICES = [
    ('1', 'First'),
    ('2', 'Second'),
    ('3', 'Pre-Final'),
    ('4', 'Final'),
    ('5', 'Alumni'),
]

GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other')
]


class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True, unique=True)
    phone_number = models.CharField(max_length=15, null=True)
    # password = models.CharField(max_length=50, null=True)

    description = models.TextField(null=True, blank=True)
    year = models.CharField(choices=YEAR_CHOICES, max_length=6)
    year_of_passing = models.CharField(max_length=5, null=True)
    github = models.CharField(max_length=100, null=True, blank=True)
    linkedin = models.CharField(max_length=100, null=True, blank=True)
    facebook = models.CharField(max_length=100, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    codechef = models.CharField(max_length=100, null=True, blank=True)
    geeksforgeeks = models.CharField(max_length=100, null=True, blank=True)
    hackerearth = models.CharField(max_length=100, null=True, blank=True)
    others = models.CharField(max_length=100, null=True, blank=True)
    profile_pic = models.ImageField(
        upload_to='member_profile_pic', default='default.jpg')
    slug = models.SlugField(unique=True, blank=True)
    gender = models.CharField(max_length=20, null=True)
    # skills = ListCharField(
    #     base_field=models.CharField(max_length=40),
    #     size=20,
    #     max_length=(21 * 50)  # 6 * 10 character nominals, plus commas
    # )
    domain_expertise = models.CharField(max_length=100, null=True)
    registration_number = models.CharField(max_length=12, null=True)

    branch = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.first_name + '-' + self.last_name)
        slug_eixts = Member.objects.filter(slug=self.slug).exists()
        if slug_eixts:
            self.slug += '-' + str(self.user.id)
        
        if self.user:
            pass
        else:
            new_user = User.objects.create_user(
                username = self.slug,
                email = self.email,
                password = self.slug,
                first_name = self.first_name,
                last_name = self.last_name,
            )
            self.user = new_user
        super(Member, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ['first_name']


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



