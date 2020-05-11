from django.shortcuts import render, redirect, reverse
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.views import View
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from core.models import Advert, Bought, AdvertComments
from .models import Profile


class MyLoginView(LoginView):
    def get_success_url(self):
        url = self.get_redirect_url()
        return url or reverse('profile', kwargs={'user': self.request.user.username})

def Pagination(request, model, number):
    paginator = Paginator(model, number)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    index = paginator.page_range.index(page_obj.number)
    max_index = len(paginator.page_range)
    start_index = index - 4 if index >= 4 else 0
    end_index = index + 4 if index <= max_index - 4 else max_index
    page_range = paginator.page_range[start_index:end_index]
    return [page_obj, page_range]

def ProfileModelBase(request, user, model): #// base profile context model
    new_user = User.objects.get(username=user)
    user_profile = Profile.objects.get(user=new_user)
    editable = False
    if request.user.username == user:
        editable = True
    context={
        "user_profile":user_profile,
        "no_data":"No other adverts",
        "editable":editable,
        "user":user
    }
    if model is not None:
        objects = model.objects.filter(user=new_user)
        pagination = Pagination(request, objects, 5)
        context["objects"] = pagination[0]
        context["range"] = pagination[1]
    return context


class ProfileView(View):
    template = 'users_templates/profile.html'

    def get(self, request, *args, **kwargs):
        user = self.kwargs["user"]
        context = ProfileModelBase(request, user, None) 
        return render(request, self.template, context)

class ProfileBoughtView(View):
    template = 'profile_templates/bought.html'

    def get(self, request, *args, **kwargs):
        user = self.kwargs["user"]
        context = ProfileModelBase(request, user, Bought)   
        return render(request, self.template, context)

class ProfileAdvertsView(View):
    template = 'profile_templates/general_list.html'

    def get(self, request, *args, **kwargs):
        user = self.kwargs["user"]
        context = ProfileModelBase(request, user, Advert)  
        return render(request, self.template, context)

class ProfileCommentsView(View):
    template = 'profile_templates/general_list.html'

    def get(self, request, *args, **kwargs):
        user = self.kwargs["user"]
        context = ProfileModelBase(request, user, AdvertComments)  
        context["comments"] = True
        return render(request, self.template, context)

class RegisterView(View):
    template = 'users_templates/register.html'
    form_class = UserRegisterForm

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'{user} has joined the society')
            return redirect('main')
    def get(self, request):
        form = self.form_class()
        return render(request, self.template, {'form':form})

