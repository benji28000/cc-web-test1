from django.db import models

# Create your models here.

class Collec(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=False)
    date = models.DateTimeField(auto_now_add=True, blank=False)
