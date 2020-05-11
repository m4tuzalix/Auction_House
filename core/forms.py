from django import forms
from .models import Advert, AdvertComments

class AdvertForm(forms.ModelForm):
    class Meta:
        model = Advert
        fields = ["title", "category", "price", "quantity", "description", "image"]

class CommentsForm(forms.ModelForm):
    class Meta:
        model = AdvertComments
        exclude = ["user", "advert", "date", "rating"]