from django import forms
from django.contrib.auth.models import User
from .models import Timetable


class EventCreateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['start', 'end']


class TimetableUpdateForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'image', 'members']
