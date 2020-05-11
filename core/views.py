from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views import View
from .forms import AdvertForm, CommentsForm
from .models import Advert, Advert_Categories, Bought, AdvertComments
from users.views import Pagination
from django.contrib.auth.models import User
import json 

# Create your views here.
def main_web(request):
    return render(request, "main.html")

def view_advert_base(request, pk, title):
    advert = Advert.objects.get(pk=pk)
    comments = AdvertComments.objects.filter(user=advert.user)
    rating = [comment.rating for comment in comments]
        
    context = {
        'advert':advert,
        'rating':round(sum(rating) / len(rating),1)
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
            found_adverts =  Advert.objects.filter(title__icontains=search_value).order_by("id")
            if len(found_adverts) > 0:
                pagination = Pagination(request, found_adverts, 10)
                context = {
                    'objects':pagination[0],
                    'value':search_value,
                    'range':pagination[1]
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
    
class AddComment(LoginRequiredMixin, View):
    comment_form = CommentsForm
    template = "comments.html"
    
    def get(self, request, *args, **kwargs):
        form = self.comment_form()
        return render(request, self.template, {"form":form})
    
    def post(self, request, *args, **kwargs):
        form = self.comment_form(request.POST)
        if form.is_valid():
            bought_advert = Bought.objects.get(pk=int(self.kwargs["pk"]))
            new_comment = form.save(commit=False)
            new_comment.user = bought_advert.advert.user
            new_comment.advert = bought_advert
            new_comment.rating = int(request.POST["rate"])
            new_comment.save()
            messages.success(request, 'Your comments has been added')
            bought_advert.comment = True
            bought_advert.save()
        else:
            messages.warning(request, 'Something went wrong')
        return redirect("main")
        