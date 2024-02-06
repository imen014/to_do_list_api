from django.shortcuts import render
from to_do_api.models import TaskContainer, EventContainer
from to_do_api.serailizers import TaskSerializer, EventSerilizer
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet


class TaskView(ModelViewSet):

    serializer_class = TaskSerializer
    def get_queryset(self,*args,**kwargs):
        queryset = TaskContainer.objects.all()
        return queryset

class EventView(ReadOnlyModelViewSet):

    serializer_class = EventSerilizer
    def get_queryset(self,*args,**kwargs):
        queryset = EventContainer.objects.all()
        return queryset
    