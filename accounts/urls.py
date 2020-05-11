from django.urls import path
from .import views

urlpatterns = [
    path('',views.home),
    path('products/',views.about),
    path('customer/',views.customer),

]
