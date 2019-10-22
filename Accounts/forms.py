from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):

  email = forms.EmailField()

  class Meta:

        model = User
        fields = {"email", "username"}


class LoginForm(forms.Form):

  username = forms.CharField(max_length = 30, label ="Username")
  password = forms.CharField(max_length = 30, label = "Password", widget = forms.PasswordInput)

