from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from LyncUp.models import Group
from django_password_strength.widgets import PasswordStrengthInput, PasswordConfirmationInput
from crispy_forms.helper import FormHelper
from .models import Profile, Friend


class UserRegisterForm(UserCreationForm):
    # helper = FormHelper()

    email = forms.EmailField
    username = forms.CharField()
    # password1 = forms.CharField(widget=PasswordStrengthInput())
    # password2 = forms.CharField(widget=PasswordConfirmationInput())


    class Meta:
        model = User


        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


# From here
class AddFriendForm(forms.ModelForm):
    User = forms.CharField()
    class Meta:
        model = User
        fields = ['User']

class RemoveFriendForm(forms.ModelForm):
    User = forms.CharField()
    class Meta:
        model = User
        fields = ['User']