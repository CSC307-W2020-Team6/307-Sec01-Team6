from django.urls import path

import LyncUp
from .views import EventCreateView, EventDeleteView, EventListView, EventUpdateView, EventDetailView
from . import views


urlpatterns = [
    # path('', PostListView.as_view(), name='LyncUp-home'),
    path('event/list/', EventListView.as_view(), name='event-list'),
    # # path with variable
    path('event/<int:pk>/update/', EventUpdateView.as_view(), name='event-update'),
    # path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    # path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    # path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    # path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('event/new/', EventCreateView.as_view(), name='event-create'),
    path('event/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('event/<int:pk>/delete/', EventDeleteView.as_view(), name='event-delete'),
]