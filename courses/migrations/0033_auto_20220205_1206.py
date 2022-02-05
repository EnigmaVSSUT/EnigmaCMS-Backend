# Generated by Django 3.2.5 on 2022-02-05 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0032_merge_20220204_2345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='Tag',
        ),
        migrations.AddField(
            model_name='tag',
            name='articles',
            field=models.ManyToManyField(blank=True, related_name='tag_articles', to='courses.Article'),
        ),
        migrations.AddField(
            model_name='tag',
            name='is_active',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='banner_image',
            field=models.ImageField(default='article_banner_default.jpg', null=True, upload_to='ArticleBannerPics'),
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('Android', 'Android'), ('Web', 'Web'), ('Backend', 'Backend'), ('ML/AI', 'ML/AI'), ('UI/UX', 'UI/UX'), ('AR/VR', 'AR/VR'), ('CP', 'Competative Programming')], max_length=100),
        ),
        migrations.AlterField(
            model_name='article',
            name='home_page_display',
            field=models.CharField(blank=True, choices=[('Exclusive', 'Exclusive'), ('Featured', 'Featured')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('Created', 'Created'), ('Draft', 'Draft'), ('Rejected', 'Rejected'), ('Published', 'Published')], default='Draft', max_length=20),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=5000),
        ),
    ]
