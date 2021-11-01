# Generated by Django 3.2.5 on 2021-11-01 07:16

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('members', '0003_alter_member_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=3000)),
                ('description', models.TextField(blank=True, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
                ('image', models.ImageField(default='article_default.jpg', upload_to='ArticlePics')),
                ('banner_image', models.ImageField(default='article_banner_default.jpg', upload_to='ArticleBannerPics')),
                ('status', models.CharField(choices=[('Published', 'Published'), ('Rejected', 'Rejected'), ('Draft', 'Draft'), ('Created', 'Created')], default='Draft', max_length=20)),
                ('home_page_display', models.CharField(blank=True, choices=[('Featured', 'Featured'), ('Exclusive', 'Exclusive')], max_length=20, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('likes', models.IntegerField(blank=True, default=0)),
                ('visits', models.IntegerField(blank=True, default=0)),
                ('contributors', models.ManyToManyField(blank=True, related_name='other_contributors', to='members.Member')),
                ('member', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='members.member')),
            ],
        ),
        migrations.CreateModel(
            name='ArticleImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='article_default.jpg', upload_to='ArticleInnerPics')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5000)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(default='track_default.jpg', upload_to='TrackPosters')),
                ('timestamp', models.DateTimeField(blank=True, null=True)),
                ('is_active', models.BooleanField(blank=True, default=True)),
                ('articles', models.ManyToManyField(blank=True, related_name='track_articles', to='courses.Article')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.topic'),
        ),
        migrations.AddField(
            model_name='article',
            name='track',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.track'),
        ),
    ]
