from django.db import models

# Create your models here.
class Todos(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    search_time = models.DateTimeField(auto_now=True)
    