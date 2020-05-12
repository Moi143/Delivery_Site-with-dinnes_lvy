from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def home(request):
    orders_data = Order.objects.all()
    customer_data = Customer.objects.all()
    context = {'orders_show':orders_data,'customer_show':customer_data}
    return render(request, 'index.html',context)

def products(request):
    products_data = Product.objects.all()
    return render(request, 'products.html',{'products_show':products_data})

def customer(request):
    return render(request, 'customers.html')