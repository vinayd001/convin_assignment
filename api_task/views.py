from rest_framework import generics
from analyzer import models
from .serializers import TaskSerializer

# Create your views here.

class ListTask(generics.ListCreateAPIView):
    queryset = models.Task.objects.all()
    serializer_class = TaskSerializer


class DetailTask(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Task.objects.all()
    serializer_class = TaskSerializer
