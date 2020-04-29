from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_web, name="main"),
    path('add/', views.add_advert, name="advertadd"),
    path('search/', views.search_advert, name="search"),
    path('search/<int:pk>/<str:title>', views.view_advert, name="advert")
]
