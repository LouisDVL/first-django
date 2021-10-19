from rest_framework import serializers, viewsets
from .serializers import ToDoSerialized
from .models import ToDoItem

# Create your views here.


class ToDoViewSets(viewsets.ModelViewSet):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoSerialized
