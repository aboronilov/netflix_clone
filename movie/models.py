from uuid import uuid4
from django.db import models


TYPE_CHOICES = (
    ('Movie', 'Movie'),
    ('Series', 'Series')
)

AGE_CHOICES = (
    ('All', "All"), 
    ('Kids', 'Kids')
)

class Movie(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid4)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    videos = models.ManyToManyField('video')
    flyer = models.ImageField(upload_to='flyers')
    age_limit = models.CharField(max_length=10, choices=AGE_CHOICES)
    
class Video(models.Model):
    title = models.CharField(max_length=225, blank=True, null=True)
    file = models.FileField(upload_to='videos')