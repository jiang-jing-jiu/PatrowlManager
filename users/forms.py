from django.contrib.auth.forms import AuthenticationForm
from django import forms


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="用户名", max_length=250,
        widget=forms.TextInput(attrs={
            'class': 'form-control', 'name': 'username', 'value': ''}))
    password = forms.CharField(
        label="密码", max_length=250,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 'name': 'password', 'value': ''}))
