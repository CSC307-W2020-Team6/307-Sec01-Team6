from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.models import User
from .models import Timetable, Event
from django.forms.fields import DateField


class DateInput(forms.DateInput):
    input_type = "date"

    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%d"
        super().__init__(**kwargs)


class TimeInput(forms.TimeInput):
    input_type = "time"


class DateTimeInput(forms.DateTimeInput):
    input_type = "datetime-local"

    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%dT%H:%M"
        super().__init__(**kwargs)


class EventCreateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["date"] = DateField(widget=AdminDateWidget)
        self.fields["start_time"].widget = TimeInput()
        self.fields["end_time"].widget = TimeInput()


# class TimetableUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Timetable
#         fields = ['name', 'image', 'members']

