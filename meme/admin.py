from django.contrib import admin
from meme.models import Meme, Submission

# Register your models here.

admin.site.register(Meme)
admin.site.register(Submission)