from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    """
    Implement new register form
    """
    email = forms.EmailField(required=False)

    class Meta:
        """
        List of form fields
        """
        model = User
        fields = ['username', 'email', 'password1', 'password2']
