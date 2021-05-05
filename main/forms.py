from django.forms import ModelForm,TextInput
from django import forms
from .models import Description
class SellForm(forms.ModelForm):

    class Meta:
        model=Description
        fields=['book_name','edition','location','price','phone','book_image','seller']
        widgets={
            'book_name':forms.TextInput(attrs={'class': 'form-control'}),
            'edition': TextInput(attrs={'class': 'form-control'}),
            'location': TextInput(attrs={'class': 'form-control'}),
            'price': TextInput(attrs={'class': 'form-control'}),
            'phone': TextInput(attrs={'class': 'form-control'}),
            'seller': TextInput(attrs={'class': 'form-control'}),
            }