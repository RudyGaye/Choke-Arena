from django.db import models
from django.conf import settings


class Forum(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name

class Topic(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField(max_length=4000)  
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    forum = models.ForeignKey('Forum', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Post(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='posts')
    message = models.TextField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


