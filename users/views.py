from django.shortcuts import render, redirect, reverse
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.views import View
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from core.models import Advert, Bought
from .models import Profile

class MyLoginView(LoginView):
    def get_success_url(self):
        url = self.get_redirect_url()
        return url or reverse('profile', kwargs={'user': self.request.user.username})

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
        paginator = Paginator(objects, 20)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context["objects"] = page_obj
        context["range"] = paginator.page_range
    return context


class ProfileView(View):
    template = 'users_templates/profile.html'

    def get(self, request, *args, **kwargs):
        user = self.kwargs["user"]
        context = ProfileModelBase(request, user, None)   # or whoever `user` is
        return render(request, self.template, context)

class ProfileBoughtView(View):
    template = 'profile_templates/bought.html'

    def get(self, request, *args, **kwargs):
        user = self.kwargs["user"]
        context = ProfileModelBase(request, user, Bought)   # or whoever `user` is
        return render(request, self.template, context)

class ProfileAdvertsView(View):
    template = 'profile_templates/general_list.html'

    def get(self, request, *args, **kwargs):
        user = self.kwargs["user"]
        context = ProfileModelBase(request, user, Advert)   # or whoever `user` is
        return render(request, self.template, context)

class ProfileCommentsView(View):
    template = 'profile_templates/general_list.html'

    def get(self, request, *args, **kwargs):
        user = self.kwargs["user"]
        context = ProfileModelBase(request, user, Advert)   # or whoever `user` is
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
