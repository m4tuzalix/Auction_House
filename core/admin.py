from django.contrib import admin
from .models import Advert, Bought, AdvertComments
from users.models import Profile

models = [Advert, Profile, Bought, AdvertComments]
for model in models:
    admin.site.register(model)
# Register your models here.
