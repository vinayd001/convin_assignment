from rest_framework import serializers
from analyzer import models


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'task_type',
            'task_desc',
        )
        model = models.Task
