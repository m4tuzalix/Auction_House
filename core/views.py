from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views import View
from django.core.paginator import Paginator
from .forms import AdvertForm
from .models import Advert, Advert_Categories, Bought
from django.contrib.auth.models import User
import json 

# Create your views here.
def main_web(request):
    return render(request, "main.html")

def view_advert_base(request, pk, title):
    advert = Advert.objects.get(pk=pk)
    context = {
        'advert':advert
    }
    return render(request, "advert.html", context)

class AddAdvertView(LoginRequiredMixin, View):
    login_url = "login"
    template = "advertadd.html"

    def post(self, request, *args, **kwargs):
        form = AdvertForm(request.POST, request.FILES)
        if form.is_valid():
            new_advert = form.save(commit=False)
            new_advert.user = User.objects.get(pk=request.user.id)
            new_advert.save()
            messages.success(request, 'Your advert has been created')
        else:
            messages.warning(request, 'Something went wrong')
        return redirect("advertadd")
    def get(self, request, *args, **kwargs):
        form = AdvertForm()
        return render(request, self.template, {'form':form})

class SearchAdvertView(View):
    template = "search.html"

    def post(self, request, *args, **kwargs):
            search_value = request.POST["search_value"]
            found_adverts =  [obj for obj in Advert.objects.all() if search_value.casefold() in obj.title] #// creates new list
            if len(found_adverts) > 0:
                paginator = Paginator(found_adverts, 10)
                page_number = request.GET.get('page')
                page_obj = paginator.get_page(page_number)
                context = {
                    'found_adverts':page_obj,
                    'value':search_value,
                    'range':paginator.page_range
                }
                return render(request, self.template, context)
            else:
                messages.warning(request, 'No results found')
            return redirect("main")

class ConfirmationView(View):
    template = "confirmation.html"

    def post(self, request, *args, **kwargs):
        amount = request.POST["amount"]
        advert = Advert.objects.get(pk=self.kwargs["pk"])
        price = advert.final_price(int(amount))
        data = [advert.title, amount, price, advert.user.username]
        context = {
            "objects":data,
            "advert":advert
        }
        request.session["data"] = [advert.id, amount, price]
        return render(request, self.template, context)

class BuyView(View):
    def post(self, request, *args, **kwargs):
        if request.session.get("data"):
            unpacked = request.session.pop("data")
            advert = Advert.objects.get(pk=unpacked[0]) #/ gets advert and substracts the given amount
            if advert.quantity > 0:
                advert.quantity -= int(unpacked[1])
                advert.save()
            else:
                advert.archive = True #/ Archives advert
                advert.save()
            bought = Bought.objects.create(user=request.user, advert=advert, amount=unpacked[1], price=unpacked[2]) #/ assigns advert to user's profile
            bought.save()
            messages.success(request, f'You have bought the item from {advert.user.username}, it is available on your profile now')
        else:
            messages.error(request, "Something has gone wrong")
        return redirect("main")
    
