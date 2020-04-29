from django import forms
from .models import Advert

class AdvertForm(forms.ModelForm):
    class Meta:
        model = Advert
        fields = ["title", "category", "price", "quantity", "description", "image"]