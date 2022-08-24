from rest_framework import routers
from django.urls import path
from meme import views


app_name = 'meme'


urlpatterns = [
    path("",views.ListMemeAPIView.as_view()),
    path("memes/<int:pk>/", views.RetrieveMemeAPIView.as_view()),
    path("add/", views.CreateMemeAPIView.as_view()),
    path("memes/<int:pk>/update/",views.UpdateMemeAPIView.as_view()),
    path("memes/submissions/", views.ListSubmissionAPIView.as_view()),
    path("memes/submissions/add/", views.CreateSubmissionAPIView.as_view())
]