import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Task(models.Model):
    TYPE1 = 1
    TYPE2 = 2
    TYPE3 = 3
    TYPE4 = 4
    TASK_TYPE = [
        (TYPE1, 1),
        (TYPE2, 2),
        (TYPE3, 3),
        (TYPE4, 4),
    ]
    task_type = models.IntegerField(choices=TASK_TYPE, default=TYPE1)
    task_desc = models.TextField(max_length=200)

    def __str__(self):
        return self.task_desc


class TaskTracker(models.Model):
    TYPE1 = 1
    TYPE2 = 2
    TYPE3 = 3
    TYPE4 = 4
    TASK_TYPE = [
        (TYPE1, 1),
        (TYPE2, 2),
        (TYPE3, 3),
        (TYPE4, 4),
    ]
    DAILY = 'Daily'
    WEEKLY = 'Weekly'
    MONTHLY = 'Monthly'
    UPDATE_TYPE = [
        (DAILY, 'Daily, Every day'),
        (WEEKLY, 'Weekly, Every Monday'),
        (MONTHLY, 'Monthly, First day of every Month'),
    ]
    task_type = models.IntegerField(choices=TASK_TYPE, default=TYPE1)
    update_type = models.CharField(max_length=32, choices=UPDATE_TYPE, default=DAILY)
    email = models.EmailField(unique=True)