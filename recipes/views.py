from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def home(requests):
    return HttpResponse('home')

def sobre(requests):
    return HttpResponse('sobre')

def contato(resquests):
    return HttpResponse('contato')