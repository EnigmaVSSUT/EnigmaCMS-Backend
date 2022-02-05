# Generated by Django 3.2.5 on 2022-02-05 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0034_auto_20220205_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('Published', 'Published'), ('Draft', 'Draft'), ('Created', 'Created'), ('Rejected', 'Rejected')], default='Draft', max_length=20),
        ),
    ]
