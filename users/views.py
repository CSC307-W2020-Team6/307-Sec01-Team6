from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import UserManager, BaseUserManager
from django.contrib.auth.models import User
from django.db import models
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, AddFriendForm, RemoveFriendForm
from django.contrib.auth.models import User
from .models import Friend
from .models import Profile #, Relationship
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'account created for {username}: you can now sign in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)  # instance does autofill
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Saved Successfully! :)')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)  # instance does autofill
        p_form = ProfileUpdateForm(instance=request.user.profile)


    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)
## From Here

@login_required
def add_friends(request):
    found_flag = 0
    # objects = UserManager()
    if request.method == "POST":
        f_form = AddFriendForm(request.POST, instance=request.user) #instance=request.user
        if f_form.is_valid():
            f_form.save()
            new_friend = f_form.cleaned_data.get("User")
            # friendlist = Friend.objects.filter(current_user=request.user).get()
            if len(Friend.objects.all()) > 0:
                try:
                    for u in Friend.objects.filter(current_user=request.user).get().users.all():
                        if str(u) == str(new_friend):
                            messages.warning(request, f'User is already in your friends list!')
                            return redirect('profile')
                except:
                    pass

            for user in User.objects.all(): # searches if they are a valid user
                if str(user) == str(new_friend):
                    found_flag = 1
                    break
            if found_flag == 1:
                Friend.make_friend(request.user, new_friend)
                messages.success(request, f'Friend Added!')
                return redirect('profile')
            else:
                messages.warning(request, f'No user found, can only add existing users.')
                return redirect('profile')
    else:
        f_form = AddFriendForm(instance=request.user)
    context = {
        'f_form': f_form
    }
    return render(request, 'users/addFriends.html', context) # , context

@login_required
def remove_friends(request):
    found_flag = 0
    if request.method == "POST":
        r_form = RemoveFriendForm(request.POST, instance=request.user)
        if r_form.is_valid():
            r_form.save()
            the_friend = r_form.cleaned_data.get("User")
            friendlist = Friend.objects.filter(current_user=request.user).get()
            for user in friendlist.users.all():
                if str(user) == str(the_friend):
                    found_flag = 1
                    break

            if found_flag == 1:
                Friend.remove_friend(request.user, the_friend)
                messages.success(request, f'Friend Removed.')
                return redirect('profile')
            else:
                messages.warning(request, f'Inputted user not in friends list.')
                return redirect('profile')
    else:
        r_form = RemoveFriendForm(instance=request.user)
    context = {
        'r_form': r_form
    }
    return render(request, 'users/removeFriends.html', context)


class FriendListView(ListView):
    model = Friend

    def get_context_data(self, **kwargs):
        context = super(FriendListView, self).get_context_data()
        context['friends'] = Friend.objects.filter(current_user=self.request.user)
        return context

   # context_object_name = "friends"
