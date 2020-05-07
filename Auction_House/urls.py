"""Auction_House URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as users_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("core.urls")),
    path('login/', users_views.MyLoginView.as_view(template_name="users_templates/login.html"), name='login'),
    path('register/', users_views.RegisterView.as_view(), name="register"),
    path('profile/<str:user>', users_views.ProfileView.as_view(), name='profile'),
    path('profile/bought/<str:user>', users_views.ProfileBoughtView.as_view(), name='bought'),
    path('profile/all_adverts/<str:user>', users_views.ProfileAdvertsView.as_view(), name='all_adverts'),
    path('profile/comments/<str:user>', users_views.ProfileCommentsView.as_view(), name='comments'),
    path('logout/', auth_views.LogoutView.as_view(template_name="users_templates/logout.html"), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)