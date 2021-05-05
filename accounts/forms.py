from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm,TextInput
from .models import Profile


class LoginForm(forms.Form):
    username=forms.CharField(max_length=150,widget=TextInput(attrs={'class': 'form-control'}))
    password=forms.CharField(max_length=128,widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class SignupForm(forms.Form):
    username=forms.CharField(max_length=150,widget=TextInput(attrs={'class': 'form-control'}))
    first_name=forms.CharField(max_length=150,widget=TextInput(attrs={'class': "form-control"}))
    last_name=forms.CharField(max_length=150,widget=TextInput(attrs={'class': 'form-control'}))
    email=forms.CharField(max_length=128,widget=TextInput(attrs={'class': 'form-control'}))
    password=forms.CharField(max_length=128,widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password=forms.CharField(max_length=128,widget=forms.PasswordInput(attrs={'class': 'form-control'}))

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
    email=forms.CharField(max_length=128,widget=TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model=User
        fields=['username','email']
        widgets={
            'username':forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['image']