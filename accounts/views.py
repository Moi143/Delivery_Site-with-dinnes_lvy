from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory #this is for multipled fromset
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

def create_order(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=("products", 'status'),extra=1)
    customer = Customer.objects.get(id=pk)
    fromset = OrderFormSet(instance = customer)
    if request.method == 'POST':
        fromset = OrderFormSet(request.POST,instance = customer)
        if fromset.is_valid():
            fromset.save()
            return redirect('/')
    context = {'fromset':fromset}
    return render(request,'order_form.html',context)

def update_order(request, pk1):
    u_order = Order.objects.get(id=pk1)
    form_update = OrderForm(instance=u_order)
    if request.method == 'POST':
        # print('printing POST:', request.POST)
        form = OrderForm(request.POST, instance=u_order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'from':form_update}
    return render(request, 'order_form.html' ,context)

def delete(request, pk2):
    d_order = Order.objects.get(id=pk2)
    if request.method == 'POST':
        d_order.delete()
        return redirect("/")
    context = {'item':d_order}
    return render(request, 'delete.html',context)