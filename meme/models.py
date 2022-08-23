from audioop import add
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

class Submission(models.Model):
    topText = models.TextField()
    dateCreated = models.DateTimeField(auto_now=True)
    bottomText = models.TextField()

    memeID = models.OneToOneField(Meme, on_delete=models.CASCADE)

