
from rest_framework import viewsets

from meme.serializers import MemeSerializer
from meme.models import Meme

class MemeViewSet(viewsets.ModelViewSet):
    queryset = Meme.objects.all()
    serializer_class = MemeSerializer
    