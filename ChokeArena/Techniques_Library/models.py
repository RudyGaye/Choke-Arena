from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='types', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Position(models.Model):
    POSITION_CHOICES = [
        ('Standing', 'Standing'),
        ('Guard', 'Guard'),
        ('Mount', 'Mount'),
        ('Side Control', 'Side Control'),
        ('Back Control', 'Back Control'),
        ('Knee on Belly', 'Knee on Belly'),
    ]

    name = models.CharField(max_length=50, unique=True, choices=POSITION_CHOICES)


class Technique(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    video_url = models.URLField()
    category = models.ForeignKey(Category, related_name='techniques', on_delete=models.CASCADE)
    type = models.ForeignKey(Type, related_name='techniques', on_delete=models.CASCADE)
    position = models.ForeignKey(Position, related_name='techniques', on_delete=models.CASCADE)
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followed_techniques')

    def __str__(self):
        return self.name
