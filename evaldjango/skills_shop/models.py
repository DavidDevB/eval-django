from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=20)


class Skill(models.Model):
    name = models.CharField(max_length=20)


class Demande(models.Model):
    activity = models.CharField(max_length=200)
    skill = models.CharField(max_length=15)
    slot = models.DateTimeField()