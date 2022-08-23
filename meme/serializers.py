from rest_framework import serializers
from meme.models import Meme, Submission

class MemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meme
        fields = "__all__"

class SubmissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Submission
        fields = "__all__"