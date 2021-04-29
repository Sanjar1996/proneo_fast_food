from django import forms
from .models import Users


class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ('username', 'email', 'first_name', 'last_name', 'password')
