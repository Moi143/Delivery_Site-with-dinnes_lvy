from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'index.html')

def products(request):
    return render(request, 'products.html')

def customer(request):
    return HttpResponse("this is my about page and my name is mayur kumar bhure")