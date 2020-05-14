from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm
# Create your views here.

def home(request):
    orders_data = Order.objects.all()
    customer_data = Customer.objects.all()

    total_customers = orders_data.count()
    total_orders = customer_data.count()
    total_delivered = orders_data.filter(status='Delivered').count()
    total_pending = orders_data.filter(status='pending').count()
    
    context = {'orders_show':orders_data,'customer_show':customer_data,'total_orders_show':total_customers,'order_delivered_show':total_delivered,'total_pending_show':total_pending}
    return render(request, 'index.html',context)

def products(request):
    products_data = Product.objects.all()
    return render(request, 'products.html',{'products_show':products_data})

def customer(request, pk_text):
    customer = Customer.objects.get(id=pk_text)
    orders = customer.order_set.all()
    total_orders = orders.count()
    context = {'customer':customer,'orders':orders,'order_counts':total_orders}
    return render(request, 'customers.html',context)

def create_order(request):
    from_data = OrderForm()

    if request.method == 'POST':
        # print('printing POST:', request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'from_data':from_data}
    return render(request,'order_form.html',context)
