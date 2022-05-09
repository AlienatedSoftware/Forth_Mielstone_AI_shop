from django.db import models

# Create your models here.

class Nft(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=200, default='information about NFT here')
    rating = models.IntegerField(default='00')
    pub_date = models.DateTimeField('date published')