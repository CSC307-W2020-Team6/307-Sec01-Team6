from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import UserManager, BaseUserManager
from django.contrib.auth.models import User
from django.db import models
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, AddFriendForm
from django.contrib.auth.models import User
from friendship.models import Friend
from .models import Profile, Relationship



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
    # objects = UserManager()
    if request.method == "POST":
        f_form = AddFriendForm(request.POST, instance=request.user) #instance=request.user
        if f_form.is_valid():
            f_form.save()

            messages.success(request, f'Friend Added!')
            return redirect('profile')
    else:
        f_form = AddFriendForm(instance=request.user)

    context = {
        'f_form':f_form
    }
    # f_form = AddFriendForm(request.POST, instance=request.user)
    # username = f_form
    # if request.user.is_authenticated == True:
    #     user = Profile.objects.get_by_natural_key(username)
    #     Relationship.objects.get_or_create(
    #         from_person=request.user,
    #         to_person=user)
    #     # return HttpResponseRedirect('/profile/')
    # context = {
    #     'f_form':f_form
    # }

    return render(request, 'users/addFriends.html', context)
    # n_f = get_object_or_404(User, username=username)
    # owner = request.user.userprofile
    # new_friend = User.objects.get(user=n_f)
    #
    # if verb == "add":
    #     new_friend.followers.add(owner)
    #     Friend.make_friend(owner, new_friend)
    # else:
    #     new_friend.followers.remove(owner)
    #     Friend.remove_friend(owner, new_friend)
    #
    # return redirect(new_friend.get_absolute_url())
