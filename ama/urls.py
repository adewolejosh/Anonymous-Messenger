from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('adminDHBD/', views.adminS, name='adminS'),
]
