from django.db import models

# Create your models here.
class Players(models.Model):
    name = models.CharField(max_length=200)
    wins = models.IntegerField(default=0)
    loss = models.IntegerField(default=0)
    online = models.BooleanField(default=True)