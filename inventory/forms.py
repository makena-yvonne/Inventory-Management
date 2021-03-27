from django import forms
from .models import *

class KitchenwareForm(forms.ModelForm):
    class Meta:
        model = Kitchenware
        fields = ('type', 'quantity', 'status', 'description')


class ChickenForm(forms.ModelForm):
    class Meta:
        model = Chicken
        fields = ('type', 'quantity', 'status', 'description')