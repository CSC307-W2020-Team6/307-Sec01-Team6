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
    success_url = '/'

    # test used to see if user can get to page
    def test_func(self):
        event = self.get_object()
        if self.request.user == event.owner:
            return True
        return False


class EventListView(ListView):
    model = Event


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
