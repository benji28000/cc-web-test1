from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Collec(models.Model):
    title = models.CharField(max_length=100,null=False)
    description = models.TextField(null=False)
    date = models.DateTimeField(auto_now_add=True,null=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='collections')

    def __str__(self):
        return self.title

class Element(models.Model):
    title = models.CharField(max_length=50,null=False)
    description = models.TextField(null=False)
    value = models.FloatField(null=False)
    quantity = models.IntegerField(null=False)
    date = models.DateTimeField(auto_now_add=True,null=False)
    collec = models.ForeignKey(Collec,on_delete=models.CASCADE, related_name='elements')
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='elements')

    def __str__(self):
        return self.title