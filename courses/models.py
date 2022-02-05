from django.db import models
import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from dateutil.relativedelta import relativedelta
from members.models import Member
from django_mysql.models import ListCharField
ARTICLE_STATUS = {
    ('Draft', 'Draft'),
    ('Created', 'Created'),
    ('Published', 'Published'),
    ('Rejected', 'Rejected')
}

CATEGORY_CHOICES = [
    ('Android', 'Android'),
    ('Web', 'Web'),
    ('Backend', 'Backend'),
    ('ML/AI', 'ML/AI'),
    ('UI/UX', 'UI/UX'),
    ('AR/VR', 'AR/VR'),
    ('CP','Competative Programming')
]

HOME_PAGE_DISPLAY_TYPES = {
    ('Featured', 'Featured'),
    ('Exclusive', 'Exclusive')
}

class Tag(models.Model):
    name = models.CharField(max_length=5000)
    slug = AutoSlugField(populate_from='name', unique=True)
    is_active = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, blank=True)
    contributors = models.ManyToManyField(Member, related_name="other_contributors", blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    name = models.CharField(max_length=3000)
    description = models.TextField(null=True, blank=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=100)
    content = models.TextField(null=True, blank=True)
    slug = AutoSlugField(populate_from='name', unique=True)
    image = models.ImageField(upload_to='ArticlePics',
                              default='article_default.jpg', blank=True)
    banner_image = models.ImageField(
        upload_to='ArticleBannerPics', default='article_banner_default.jpg', null=True, blank=True)
    status = models.CharField(
        max_length=20, choices=ARTICLE_STATUS, default='Draft')
    home_page_display = models.CharField(
        max_length=20, choices=HOME_PAGE_DISPLAY_TYPES, null=True, blank=True)
    likes = models.IntegerField(default=0)
    track = models.ForeignKey(
        'Track', on_delete=models.CASCADE, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0, blank=True)
    visits = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        try:
            track = self.track
            super(Article, self).save(*args, **kwargs)
            track.articles.add(self)
        except:
            super(Article, self).save(*args, **kwargs)


class ArticleImage(models.Model):
    image = models.ImageField(
        upload_to='ArticleInnerPics', default='article_default.jpg')
    name = models.TextField()

    # def __str__(self):
    #     return self.image


class Track(models.Model):
    name = models.CharField(max_length=5000)
    slug = AutoSlugField(populate_from='name', unique=True)
    description = models.TextField(null=True, blank=True)
    articles = models.ManyToManyField(
        Article, related_name='track_articles', blank=True)
    image = models.ImageField(upload_to='TrackPosters',
                              default='track_default.jpg')
    timestamp = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.timestamp:
            self.timestamp = timezone.now()
        super(Track, self).save(*args, **kwargs)

