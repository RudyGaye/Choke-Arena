from django.db import models
from django.conf import settings
import re

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
    name = models.CharField(max_length=50)



class Technique(models.Model):
    
    name = models.CharField(max_length=200)
    description = models.TextField()
    video_url = models.URLField()
    category = models.ForeignKey(Category, related_name='techniques', on_delete=models.CASCADE)
    type = models.ForeignKey(Type, related_name='techniques', on_delete=models.CASCADE)
    position = models.ForeignKey(Position, related_name='techniques', on_delete=models.CASCADE)
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followed_techniques')
    
    def convert_video_url(self):
        match = re.match(r'^https://www\.bitchute\.com/video/([^/]+)/$', self.video_url)
        if match:
            video_id = match.group(1)
            return f'https://www.bitchute.com/embed/{video_id}/'
        return self.video_url

    def save(self, *args, **kwargs):
        # Modify the video URL before saving
        self.video_url = self.convert_video_url()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

