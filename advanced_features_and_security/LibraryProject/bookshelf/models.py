from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    def __str__(self):
        return self.username

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    class Meta:
        permissions = [
            ('can_view', 'Can view article'),
            ('can_create', 'Can create article'),
            ('can_edit', 'Can edit article'),
            ('can_delete', 'Can delete article'),
        ]
    
    def __str__(self):
        return self.title

