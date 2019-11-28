from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm

class UserCustomCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'password1', 'password2')