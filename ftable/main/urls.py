from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('mcl', views.mcl),
    path('mfl', views.mfl),
    path('mbl', views.mbl)
]
