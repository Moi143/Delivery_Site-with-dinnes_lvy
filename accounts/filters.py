import django_filters
from django_filters import CharFilter, DateFilter
from .models import *
from django.forms.widgets import TextInput
class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name = "date_created" , lookup_expr='gte',widget=TextInput(attrs={'placeholder': 'Month/Date/Year'}))
    end_date = DateFilter(field_name = "date_created" , lookup_expr='lte',widget=TextInput(attrs={'placeholder': 'Month/Date/Year'}))
    notes = CharFilter(field_name = "notes", lookup_expr='icontains',widget=TextInput(attrs={'placeholder': 'Notes'}))
    class Meta:
        model = Order
        fields = "__all__"
        exclude = ['customer','date_created']
