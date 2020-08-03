from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Profile


class LoginForm(forms.Form):
    username=forms.CharField(max_length=150)
    password=forms.CharField(max_length=128,widget=forms.PasswordInput())

class SignupForm(forms.Form):
    username=forms.CharField(max_length=150)
    first_name=forms.CharField(max_length=150)
    last_name=forms.CharField(max_length=150)
    email=forms.CharField(max_length=128)
    password=forms.CharField(max_length=128,widget=forms.PasswordInput())
    confirm_password=forms.CharField(max_length=128,widget=forms.PasswordInput())

    def clean_username(self):
        if User.objects.filter(username=self.cleaned_data['username']).exists():
            raise forms.ValidationError('This username is taken')
        return self.cleaned_data['username']


    def clean(self):
        password=self.cleaned_data['password']
        confirm_password=self.cleaned_data['confirm_password']
        if password !=confirm_password:
            raise forms.ValidationError('Password donot match')

class UserUpdateForm(forms.ModelForm):
    email=forms.CharField(max_length=128)
    class Meta:
        model=User
        fields=['username','email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['image']