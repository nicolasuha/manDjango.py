from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import AutomobileForm

def index(request):
    return render(request,'voitures/index.html')

def formulaire(request):
    return render(request, 'voitures/formulaire.html')

def ajout(request):
