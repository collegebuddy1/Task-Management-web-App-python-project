from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.
class Goal(models.Model):
    name = models.CharField(max_length=200, null=True, unique=True) # not null
    priority = models.PositiveSmallIntegerField(blank=True)
    reason = models.CharField(max_length=200, blank=True)
    informations = models.CharField(max_length=200, blank=True)

class Task(models.Model):
    task_name = models.CharField(max_length=200, null=True) # not null
    task_goal = models.CharField(max_length=200, blank=True)
    task_priority = models.PositiveSmallIntegerField(blank=True)
    task_reason = models.CharField(max_length=200, blank=True)
    task_duration = models.IntegerField(default=1)
    task_informations = models.CharField(max_length=200, blank=True)
    task_done = models.BooleanField(default=False)
    task_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)


class Day(models.Model):
    date = models.DateField()
    daily_tasks = models.ManyToManyField(Task)

