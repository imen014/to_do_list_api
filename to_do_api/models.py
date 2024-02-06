from django.db import models

class TaskContainer(models.Model):
    title = models.CharField(max_length=50)
    writer = models.CharField(max_length=50)
    description=models.CharField(max_length=255)

class EventContainer(models.Model):
    title=models.CharField(max_length=50)
    creator=models.CharField(max_length=50)
    status=models.CharField(max_length=50)
    number=models.IntegerField()