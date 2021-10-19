from django.db import models

# Create your models here.


class ToDoItem(models.Model):
    task = models.CharField(max_length=60)
    dateCreated = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.task
