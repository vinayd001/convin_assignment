from rest_framework import serializers
from analyzer import models


class TaskTrackerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'task_type',
            'update_type',
            'email',
        )
        model = models.TaskTracker
