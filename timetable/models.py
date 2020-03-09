from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import datetime


class Event(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='event_owner')
    event_name = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.event_name


class Timetable(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='timetable_owner')
    busy = models.ManyToManyField(Event)

    # 1. Make an event model that has a name date start and end times. Add to busy = models.Many...
    # 2.

    def __str__(self):
        return f'{self.owner.username}s Timetable'
