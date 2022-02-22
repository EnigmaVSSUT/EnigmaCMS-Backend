# Generated by Django 3.2.5 on 2022-02-22 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0019_auto_20220222_2142'),
        ('members', '0005_rename_new_domain_expertise_member_domain_expertise'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='domain_expertise',
        ),
        migrations.AddField(
            model_name='member',
            name='domain_expertise',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='DOMAIN_EXPERTISE', to='courses.domain'),
        ),
    ]