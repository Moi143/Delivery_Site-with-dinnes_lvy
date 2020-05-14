from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('products/',views.products,name='products'),
    path('customer_profile/<str:pk_text>/',views.customer,name='customer'),
    path('create_order',views.create_order,name="Create_Order"),
]