from django.db import models

# Create your models here.

class Command(models.Model):
    cmd = models.TextField()
