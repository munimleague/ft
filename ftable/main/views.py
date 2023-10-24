from os import link
from django.shortcuts import render
from .models import tatal, lik

def index(request):
    return render(request, 'main/index.html')

def mcl(request):
    return render(request, 'main/mcl.html')

def mfl(request):
    table = tatal.objects.all()
    link = lik.objects.all()
    return render(request, 'main/mfl.html', {'table':table, 'link':link})

def mbl(request):
    return render(request, 'main/mbl.html')