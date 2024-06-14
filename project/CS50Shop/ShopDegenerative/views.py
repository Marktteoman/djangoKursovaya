from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    return HttpResponse('Старинца приложения магазина')

def categories(request, catId):
    return HttpResponse(f'Категории приложения {catId}')

