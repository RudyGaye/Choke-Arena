# training_plans/models.py
from django.db import models
from Techniques_Library.models import Technique
from django.conf import settings


class TrainingPlan(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    techniques = models.ManyToManyField(Technique)
    difficulty = models.IntegerField()  
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followed_training_plans')
