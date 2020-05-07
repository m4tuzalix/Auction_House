from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_web, name="main"),
    path('add/', views.AddAdvertView.as_view(), name="advertadd"),
    path('search/', views.SearchAdvertView.as_view(), name="search"),
    path('search/<int:pk>/<str:title>', views.view_advert_base, name="advert"),
    path('archive/<int:pk>/<str:title>', views.view_advert_base, name="archive"),
    path('confirmation/<int:pk>/<str:title>', views.ConfirmationView.as_view(), name="confirmation"),
    path('buy/<int:pk>/<str:title>', views.BuyView.as_view(), name="buy"),
]
