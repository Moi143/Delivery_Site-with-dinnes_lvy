from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('products/',views.products,name='products'),
    path('customer_profile/<str:pk_text>/',views.customer,name='customer'),
    
    path('create_order/<str:pk>/',views.create_order,name="create_order"),
    path('Update_order/<str:pk1>/',views.update_order,name='update'),
    path('delete_order/<str:pk2>/',views.delete,name='delete'),
]