from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory #this is for multipled fromset
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import OrderForm, CreateUserForm
from .filters import OrderFilter
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def registerpage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            messages.success(request, 'Account is created for ' + first_name + " " + last_name )
            return redirect('login')
    context = {'form':form}
    return render(request, 'register14.html', context)

def loginpage(request):
    if request.method == 'POST':
        username1 = request.POST.get('username')
        password1 = request.POST.get('password')
        user = authenticate(request, username=username1 , password=password1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request,'Username or Password is not Valid')
    context = {}
    return render(request,'login14.html',context)

def logoutuser(request):
    logout(request)
    return redirect('login')

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
    myfilter = OrderFilter(request.GET, queryset=orders)
    orders = myfilter.qs
    context = {'customer':customer,'orders':orders,'order_counts':total_orders,'myfilter':myfilter}
    return render(request, 'customers.html',context)

def create_order(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=("products", 'status'),extra=10)
    customer = Customer.objects.get(id=pk)
    fromset = OrderFormSet(queryset=Order.objects.none(),instance = customer)
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