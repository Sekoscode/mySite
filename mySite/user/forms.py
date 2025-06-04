from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    """
    Form for registering a new user.

    Inherits from Django's built-in UserCreationForm and specifies
    the User model along with the fields to include in the form:
    'username', 'password1', and 'password2' for password confirmation.

    Attributes:
        Meta (class): Contains metadata for the form including the model
                      and fields to use.
    """
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
