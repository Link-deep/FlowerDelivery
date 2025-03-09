from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'main/index.html')

def products(request):
    data = {
        "caption":"Название продукта"
    }
    return HttpResponse(" request, {'caption': 'Название продукта'} ")

def cart(request):
    return HttpResponse("<h1>Это страница about на Django</h1>")


