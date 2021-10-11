from django.db import models
import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from dateutil.relativedelta import relativedelta
from members.models import Member

ARTICLE_STATUS = {
    ('Draft', 'Draft'),
    ('Created', 'Created'),
    ('Published', 'Published'),
    ('Rejected', 'Rejected')
}

HOME_PAGE_DISPLAY_TYPES = {
    ('Featured', 'Featured'),
    ('Exclusive', 'Exclusive')
}

class Section(models.Model):
    name= models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='name', unique=True)

    def __str__(self):
        return self.name



class Article(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, blank=True)
    contributors = models.ManyToManyField(Member, related_name="other_contributors", blank=True)
    section = models.ForeignKey(Section,on_delete=models.CASCADE)
    name = models.CharField(max_length=3000)
    description = models.TextField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    slug = AutoSlugField(populate_from='name', unique=True)
    image = models.ImageField(upload_to='ArticlePics', default='article_default.jpg')
    banner_image = models.ImageField(upload_to='ArticleBannerPics', default='article_banner_default.jpg')
    status = models.CharField(max_length=20, choices=ARTICLE_STATUS, default='Draft')
    home_page_display = models.CharField(max_length=20, choices=HOME_PAGE_DISPLAY_TYPES, null=True, blank=True)
    likes = models.IntegerField(default=0)
    edition = models.ForeignKey('Edition', on_delete=models.CASCADE, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0, blank=True)
    visits = models.IntegerField(default=0, blank=True)
    

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        try:
            ed = self.edition
            super(Article, self).save(*args, **kwargs)
            ed.articles.add(self)
        except:
            super(Article, self).save(*args, **kwargs)

class ArticleImage(models.Model):
    image = models.ImageField(upload_to='ArticleInnerPics', default='article_default.jpg')
    name = models.TextField()

    # def __str__(self):
    #     return self.image

class Edition(models.Model):
    name = models.CharField(max_length=5000)
    slug = AutoSlugField(populate_from='name', unique=True)
    description = models.TextField(null=True, blank=True)
    articles = models.ManyToManyField(Article, related_name='edition_articles', blank=True)
    image = models.ImageField(upload_to='EditionPics', default='edition_default.jpg')
    timestamp = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True, blank=True)


    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.timestamp:
            self.timestamp = timezone.now()
        super(Edition, self).save(*args, **kwargs)