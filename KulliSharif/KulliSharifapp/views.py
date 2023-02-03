from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.generics import ListAPIView,RetrieveAPIView
# Create your views here.

# Events
class EventsListApiView(ListAPIView):
    queryset=Events.objects.all()
    serializer_class=EventSerializers
class EventsRetriveApiView(RetrieveAPIView):
    queryset=Events.objects.all()
    serializer_class=EventSerializers

#Projects  
class ProjectsListApiView(ListAPIView):
    queryset=Projects.objects.all()
    serializer_class=ProjectSerializers
class ProjectsRetriveApiView(RetrieveAPIView):
    queryset=Projects.objects.all()
    serializer_class=ProjectSerializers

# Books
class BooksListApiView(ListAPIView):
    queryset=Books.objects.all()
    serializer_class=BooksSerializers
class BooksRetriveApiView(RetrieveAPIView):
    queryset=Books.objects.all()
    serializer_class= BooksSerializers

# videos
class VideosListApiView(ListAPIView):
    queryset=Videos.objects.all()
    serializer_class=VideoSerializers
class VideosRetriveApiView(RetrieveAPIView):
    queryset=Videos.objects.all()
    serializer_class=VideoSerializers        





