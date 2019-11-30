from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from users.models import Profile


class UserRegisterForm(UserCreationForm):
    """ Implement new register form """
    email = forms.EmailField(required=False)

    class Meta:
        """ List of form fields """
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    """ profile update form """
    email = forms.EmailField(required=False)

    class Meta:
        """ form fields """
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    """ image update form """
    class Meta:
        """ form fields """
        model = Profile
        fields = ['image']
