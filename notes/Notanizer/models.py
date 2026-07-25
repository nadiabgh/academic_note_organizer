from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
    def __str__(self):
        return self.username
    
class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    
class Note(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='notes')
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title


