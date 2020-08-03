from django.forms import ModelForm
from .models import Description
class SellForm(ModelForm):
    class Meta:
        model=Description
        fields=['book_name','edition','location','price','phone','book_image','seller']