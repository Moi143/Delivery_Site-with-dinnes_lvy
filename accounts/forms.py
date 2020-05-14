from django.forms import ModelForm
from .models import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order
        # fields = ['Customer','Order']
        fields = '__all__'