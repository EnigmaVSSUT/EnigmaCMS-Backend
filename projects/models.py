from django.db import models
from members.models import Member
from django_mysql.models import ListCharField

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    tect_stack = ListCharField(
        base_field=models.CharField(max_length=40),
        size=20,
        max_length=(21 * 50)  # 6 * 10 character nominals, plus commas
    )

    def __str__(self):
        return self.name

