from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, GroupListView, GroupDetailView,  GroupUpdateView, GroupDeleteView
from . import views


urlpatterns = [
    path('', PostListView.as_view(), name='LyncUp-home'),
    path('group/list/', GroupListView.as_view(), name='group-list'),
    # path with variable
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('group/<int:pk>/', GroupDetailView.as_view(), name='group-detail'),
    path('group/<int:pk>/update/', GroupUpdateView.as_view(), name='group-update'),
    path('group/<int:pk>/delete/', GroupDeleteView.as_view(), name='group-delete'),
    path('about/', views.about, name='LyncUp-about'),
]