# Generated by Django 3.2.5 on 2022-02-21 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_auto_20220221_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='home_page_display',
            field=models.CharField(blank=True, choices=[('Featured', 'Featured'), ('Exclusive', 'Exclusive')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('Published', 'Published'), ('Created', 'Created'), ('Rejected', 'Rejected'), ('Draft', 'Draft')], default='Draft', max_length=20),
        ),
    ]