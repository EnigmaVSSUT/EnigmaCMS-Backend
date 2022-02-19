# Generated by Django 3.2.5 on 2022-02-19 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_alter_article_home_page_display'),
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
            field=models.CharField(choices=[('Rejected', 'Rejected'), ('Created', 'Created'), ('Draft', 'Draft'), ('Published', 'Published')], default='Draft', max_length=20),
        ),
    ]
