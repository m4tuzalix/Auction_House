from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import AdvertForm
from .models import Advert, Advert_Categories

# Create your views here.
def main_web(request):
    return render(request, "main.html")

def view_advert(request, pk, title):
    advert = Advert.objects.get(pk=pk)
    return render(request, "advert.html", {'advert':advert})

def add_advert(request):
    if request.method == "POST":
        form = AdvertForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            title = form.cleaned_data["title"]
            category = form.cleaned_data["category"]
            price = form.cleaned_data["price"]
            quantity = form.cleaned_data["quantity"]
            description = form.cleaned_data["description"]
            image = form.cleaned_data["image"]
            advert = Advert.objects.create(user=user, title=title, category=category, price=price, quantity=quantity, description=description, image=image)
            messages.success(request, 'Your advert has been created')
        else:
            messages.warning(request, 'Something went wrong')
        return redirect("advertadd")
    else:
        form = AdvertForm()
        return render(request, "advertadd.html", {'form':form})

def search_advert(request):
    if request.method == "POST":
        search_value = request.POST["search_value"]
        found_adverts =  [obj for obj in Advert.objects.all() if search_value in obj.title] #// creates new list
        if len(found_adverts) > 0:
            context = {
                'found_adverts':found_adverts,
                'value':search_value
            }
            return render(request, "search.html", context)
        else:
            messages.warning(request, 'No results found')
    return redirect("main")
    
