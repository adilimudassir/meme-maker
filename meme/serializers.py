from rest_framework import serializers
from meme.models import Meme

class MemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meme
        fields = "__all__"