from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def home(requests):
    return render(requests, 'recipes/home.html')

def sobre(requests):
    return render(requests, 'recipes/sobre')

def contato(resquests):
    return render(requests, 'recipes/contato')