
from rest_framework import generics

from meme.serializers import MemeSerializer, SubmissionSerializer
from meme.models import Meme, Submission

class ListMemeAPIView(generics.ListAPIView):
    """Lists all Memes from the database"""
    queryset = Meme.objects.all()
    serializer_class = MemeSerializer

class RetrieveMemeAPIView(generics.RetrieveAPIView):
    """Lists all Memes from the database"""
    queryset = Meme.objects.all()
    serializer_class = MemeSerializer

class CreateMemeAPIView(generics.CreateAPIView):
    """Creates a new Meme"""
    queryset = Meme.objects.all()
    serializer_class = MemeSerializer

class UpdateMemeAPIView(generics.UpdateAPIView):
    """Update the Meme whose id has been passed through the request"""
    queryset = Meme.objects.all()
    serializer_class = MemeSerializer


class ListSubmissionAPIView(generics.ListAPIView):
    """Lists all Memes from the database"""
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer

class CreateSubmissionAPIView(generics.CreateAPIView):
    """Lists all Memes from the database"""
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    
    
    def post(self, request, *args, **kwargs):
        instance = Meme.objects.get(pk=kwargs['pk'])
        return self.create(request, *args, **kwargs)

