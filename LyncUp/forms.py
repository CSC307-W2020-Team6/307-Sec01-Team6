from django import forms
from django.contrib.auth.models import User
from .models import Group


class GroupCreateForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'image']

