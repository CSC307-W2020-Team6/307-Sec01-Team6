from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Event(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='event_owner')
    event_name = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now)
    start_time = models.TimeField(default=timezone.now)
    end_time = models.TimeField(default=timezone.now)

    def __str__(self):
        return self.event_name

    def get_absolute_url(self):
        return reverse('event-detail', kwargs={'pk': self.pk})

    def get_start_hour(self):
        return self.start_time.hour

    def get_end_hour(self):
        return self.end_time.hour

    def get_date_as_int(self):
        return self.date.weekday()


class Timetable(models.Model):

    # 1. Make an event model that has a name date start and end times. Add to busy = models.Many...
    # 2.

    def __str__(self):
        return f'{self.owner.username}s Timetable'
