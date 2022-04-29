from django.shortcuts import render

def index(request):
    return render(request,'voitures/index.html')

def formulaire(request):
    return render(request, 'voitures/formulaire.html')
