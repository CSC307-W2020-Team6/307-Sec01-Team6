from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, GroupListView, GroupDetailView, GroupCreateView, GroupUpdateView, GroupDeleteView
from . import views
from LyncUp import views as LyncUp_views


urlpatterns = [
    path('', views.home, name='LyncUp-home'),
    path('group/list/', GroupListView.as_view(), name='group-list'),
    # path with variable
    path('group/<int:pk>/update/', GroupUpdateView.as_view(), name='group-update'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('group/list/new/', GroupCreateView.as_view(), name='group'),
    path('group/<int:pk>/', GroupDetailView.as_view(), name='group-detail'),
    path('group/<int:pk>/delete/', GroupDeleteView.as_view(), name='group-delete'),
    path('about/', views.about, name='LyncUp-about'),

]