from django.db.models import fields
from .models import ToDoItem
from rest_framework import serializers


class ToDoSerialized(serializers.ModelSerializer):
    class Meta:
        model = ToDoItem
        fields = ('id', 'task', 'dateCreated')

    def validate(self, data):
        print("this is the validate method", data['task'])
        return data
