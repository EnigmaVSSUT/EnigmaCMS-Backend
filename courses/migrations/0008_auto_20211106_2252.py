# Generated by Django 3.2.5 on 2021-11-06 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_alter_article_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='home_page_display',
            field=models.CharField(blank=True, choices=[('Exclusive', 'Exclusive'), ('Featured', 'Featured')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('Created', 'Created'), ('Rejected', 'Rejected'), ('Published', 'Published'), ('Draft', 'Draft')], default='Draft', max_length=20),
        ),
    ]
