from turtle import title
from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=255)
    due_date=models.DateField()

    def __str__(self):
        return self.title
