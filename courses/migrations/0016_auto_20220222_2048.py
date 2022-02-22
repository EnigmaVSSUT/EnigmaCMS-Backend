# Generated by Django 3.2.5 on 2022-02-22 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0015_alter_article_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='domain_of_track',
            field=models.ManyToManyField(blank=True, related_name='Domain_of_tracks', to='courses.Domain'),
        ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('Published', 'Published'), ('Draft', 'Draft'), ('Created', 'Created'), ('Rejected', 'Rejected')], default='Draft', max_length=20),
        ),
        migrations.AlterField(
            model_name='domain',
            name='icon',
            field=models.CharField(choices=[('W', 'Web Dev'), ('A', 'App Dev'), ('C', 'Cyber Security'), ('G', 'Game'), ('M', 'ML/AI'), ('P', 'Competitive Programing'), ('V', 'AR/VR'), ('U', 'UI/UX')], max_length=100, null=True),
        ),
    ]