from audioop import add
from django.db import models

# Create your models here.
class Meme(models.Model):
    name = models.TextField(null=False, blank=False)
    tags = models.TextField(null=False, blank=False)
    image = models.TextField(null=False, blank=False)
    topText = models.TextField(null=True, blank=True)
    bottomText = models.TextField(null=True, blank=True)
    detail = models.TextField(null=True, blank=True)
    thumb = models.TextField(null=True, blank=True)
    rank = models.TextField(null=True, blank=True)

class Submission(models.Model):
    topText = models.TextField()
    dateCreated = models.DateTimeField(auto_now=True)
    bottomText = models.TextField()

    memeID = models.ForeignKey(Meme, on_delete=models.CASCADE)

