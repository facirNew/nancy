from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import *


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'short_view', 'content', 'photo', 'tags', 'is_published']
        widgets = {
            'tags': forms.CheckboxSelectMultiple,
        }


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': "form-control"}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': "form-control"}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': "form-control"}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': "form-control"}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': "form-control"}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': "form-control"}))

