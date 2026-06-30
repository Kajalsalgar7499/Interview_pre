from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    skills = models.TextField()
    resume = models.FileField(upload_to="resume/")
