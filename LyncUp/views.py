from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django import forms
from django.db import models
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from .models import Post, Group
from timetable.models import Event
from .forms import GroupCreateForm, GroupUpdateForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse


def home(request):
    context = {
        'posts': Post.objects.all()
    }

    return render(request, "LyncUp/home.html", context)


@login_required
def group(request, model=Group, **kwargs):

    if request.method == 'POST':
        g_form = GroupCreateForm(request.POST, request.FILES)
        if g_form.is_valid():
            g_form.save()
            messages.success(request, f'Group Made Successfully! :)')
            return redirect('group-list')
    else:
        g_form = GroupCreateForm()

    context = {
        'g_form': g_form
    }
    return render(request, 'LyncUp/group_form.html', context)


@login_required
def edit_group(request, model=Group, **kwargs):

    if request.method == 'POST':
        g_form = GroupUpdateForm(request.POST, request.FILES)
        if g_form.is_valid():
            g_form.save()
            messages.success(request, 'Group Edited Successfully! :)')
            return redirect('group-list')
    else:
        g_form = GroupUpdateForm()

    context = {
        'g_form': g_form
    }
    return render(request, 'LyncUp/group_form.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'LyncUp/home.html'
    # <app>/<model>_<viewtype>.html is default template name
    # default temp is LyncUp/post_list.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class GroupListView(ListView):
    model = Group
    context_object_name = 'groups'


class PostDetailView(DetailView):
    model = Post


def get_arr(users):
    # Creates a list containing 7 lists, each of 24 items, all set to 0
    w, h = 24, 7
    output = [[[0 for x in range(w)] for y in range(h)] for z in range(len(users))]
    i = 0

    for user in users:
        for event in Event.objects.all().filter(owner=user):
            for x in range(event.get_start_hour(), event.get_end_hour()):
                output[i][event.get_date_as_int()][x] = user.profile.image.url
        i += 1
    return output


class GroupDetailView(DetailView):
    model = Group

    def get_context_data(self, **kwargs):
        context = super(GroupDetailView, self).get_context_data()
        context['posts'] = reversed(Post.objects.all())
        context['3d_arr'] = get_arr(self.get_object().members.all())
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'group']

    def get_success_url(self):
        return reverse('group-detail', kwargs={'pk': self.object.group.pk})

    def form_valid(self, form):
        form.instance.author = self.request.user
        if form.instance.author not in form.instance.group.members.all():
            messages.warning(self.request, f'Could not post. You do not belong to {form.instance.group.name}')
            return redirect('LyncUp-home')
        return super().form_valid(form)


class GroupCreateView(LoginRequiredMixin, CreateView):
    model = Group
    fields = ['name', 'image', 'members']

    def form_valid(self, form):
        members = form.cleaned_data.get('members')
        if self.request.user not in members:
            messages.warning(self.request, 'You must add yourself to your group')
            return redirect('group')
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

    def form_valid(self, g_form):
        # g_form.instance.author = self.request.user
        return super().form_valid(g_form)

    # user verification test
    def test_func(self):
        group = self.get_object()
        if self.request.user == group.group_owner:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post

    def get_success_url(self):
        return reverse('group-detail', kwargs={'pk': self.object.group.pk})

    # test used to see if user can get to page
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class GroupDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Group
    success_url = '/group/list/'

    # test used to see if user can get to page
    def test_func(self):
        group = self.get_object()
        if self.request.user == group.group_owner:
            return True
        return False


def about(request):
    return render(request, "LyncUp/about.html", {'title': 'About'})
