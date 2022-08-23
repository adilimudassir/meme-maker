from django.db import models

# Create your models here.
class Meme(models.Model):
    name = models.TextField()
    tags = models.TextField()
    image = models.TextField()
    topText = models.TextField()
    bottomText = models.TextField()
    detail = models.TextField()
    thumb = models.TextField()
    rank = models.TextField()