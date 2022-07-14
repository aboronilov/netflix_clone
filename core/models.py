from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractUser


AGE_CHOICES = (
    ('All', "All"), 
    ('Kids', 'Kids')
)


class CustomUser(AbstractUser):
    profiles = models.ManyToManyField('Profile', null=True, blank=True)
    
    
class Profile(models.Model):
    uuid = models.UUIDField(default=uuid4)
    name = models.CharField(max_length=50)
    age_limit = models.CharField(max_length=10, choices=AGE_CHOICES)
    
