from django.urls import path

import LyncUp
from .views import EventCreateView, EventDeleteView, EventListView, EventUpdateView, EventDetailView
from . import views


urlpatterns = [
    path('event/list/', EventListView.as_view(), name='event-list'),
    path('event/<int:pk>/update/', EventUpdateView.as_view(), name='event-update'),
    path('timetable/', views.user_table, name='table'),
    path('event/new/', EventCreateView.as_view(), name='event-create'),
    path('event/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('event/<int:pk>/delete/', EventDeleteView.as_view(), name='event-delete'),
]