from django.conf import settings
from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=20)


class Skill(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Query(models.Model):
    activity = models.CharField(max_length=200)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='queries')
    slot = models.DateTimeField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='queries', null=True, blank=True
    )