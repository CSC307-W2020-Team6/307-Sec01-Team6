from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django import forms
from django.db import models
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from .models import Timetable, Event


class EventCreateView(CreateView):
    model = Event
    fields = ['event_name', 'date', 'start_time', 'end_time']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    fields = ['event_name', 'date', 'start_time', 'end_time']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def test_func(self):
        event = self.get_object()
        if self.request.user == event.owner:
            return True
        return False


class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    success_url = '/event/list'

    # test used to see if user can get to page
    def test_func(self):
        event = self.get_object()
        if self.request.user == event.owner:
            return True
        return False


class EventListView(ListView):
    model = Event
    context_object_name = 'events'


class EventDetailView(DetailView):
    model = Event

    def get_context_data(self, **kwargs):
        context = super(EventDetailView, self).get_context_data()
        context['events'] = reversed(Event.objects.all())
        return context


def user_table(request):

    def get_array(events):
        # Creates a list containing 7 lists, each of 24 items, all set to 0
        w, h = 24, 7
        output = [[0 for x in range(w)] for y in range(h)]

        for event in events:
            for x in range(event.get_start_hour(), event.get_end_hour()):
                output[event.get_date_as_int()][x] = event
        return output

    context = {
        'events': get_array(Event.objects.all().filter(owner=request.user))
    }

    return render(request, 'timetable/timetable.html', context)


class TimetableDetailView(DetailView):
    pass


class TimetableCreateView(CreateView):
    pass


class TimetableUpdateView(UpdateView):
    pass


class TimetableListView(ListView):
    pass


class TimetableDeleteView(DeleteView):
    pass
