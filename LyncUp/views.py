from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.db import models
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from .models import Post, Group
from .forms import GroupCreateForm
from django.contrib.auth.models import User


def home(request):
    context = {
        'posts': Post.objects.all()
    }

    return render(request, "LyncUp/home.html", context)


@login_required
def group(request, model=Group):

    if request.method == 'POST':
        g_form = GroupCreateForm(request.POST, request.FILES, instance=request.user)
        if g_form.is_valid():
            g_form.save()
            obj = model(**g_form.cleaned_data)
            obj.save()
            obj.members.add(request.user)
            obj.save()
            messages.success(request, f'Group Made Successfully! :)')
            return redirect('group-list')
    else:
        g_form = GroupCreateForm(instance=request.user)

    context = {
        'g_form': g_form
    }
    return render(request, 'LyncUp/group_form.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'LyncUp/home.html'
    # <app>/<model>_<viewtype>.html is default template name
    context_object_name = 'posts'
    ordering = ['-date_posted']


class GroupListView(ListView):
    model = Group
    context_object_name = 'groups'


class PostDetailView(DetailView):
    model = Post


class GroupDetailView(DetailView):
    model = Group


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # user verification test
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class GroupUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Group
    fields = ['name', 'image', 'members']

    # user verification test
    def test_func(self):
        group = self.get_object()
        if self.request.user in group.members:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    # test used to see if user can get to page
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class GroupDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Group
    success_url = '/'

    # test used to see if user can get to page
    def test_func(self):
        group = self.get_object()
        if self.request.user in group.members:
            return True
        return False


def about(request):
    return render(request, "LyncUp/about.html", {'title' : 'About'})
