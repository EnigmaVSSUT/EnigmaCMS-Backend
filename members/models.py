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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    year = models.CharField(choices=YEAR_CHOICES, max_length=6)
    github = models.CharField(max_length=100, null=True, blank=True)
    linkedin = models.CharField(max_length=100, null=True, blank=True)
    facebook = models.CharField(max_length=100, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    others = models.CharField(max_length=100, null=True, blank=True)
    profile_pic = models.ImageField(
        upload_to='member_profile_pic', default='default.jpg')
    # slug = AutoSlugField(populate_from=lambda instance: instance.title,
    #                      unique_wit9h=['user__last_name', 'user__first_name'],
    #                      slugify=lambda value: value.replace(' ','-'))
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


