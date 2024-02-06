from rest_framework.serializers import ModelSerializer
from to_do_api.models import TaskContainer, EventContainer

class TaskSerializer(ModelSerializer):
    class Meta:
        model = TaskContainer
        fields=['title','writer','description']

class EventSerilizer(ModelSerializer):
    class Meta:
        model = EventContainer
        fields=['title','creator','status','number']