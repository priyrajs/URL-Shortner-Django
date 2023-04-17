from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('shortit', views.shortit, name='shortit'),
    path('<str:url>/', views.catch_all_view),
    ]