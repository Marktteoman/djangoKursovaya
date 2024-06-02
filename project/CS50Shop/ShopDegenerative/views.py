from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    return HttpResponse("Hello World")

def profile_view(request):
    return render(request, 'profile.html')


class PanCreateView:
    pass


class PanIpdateView:
    pass


class PaDeleteView:
    pass