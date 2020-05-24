from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


from .models import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order
        # fields = ['Customer','Order']
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    username = forms.CharField(label=('Username'),max_length=150,help_text=('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),error_messages={'unique': ("A user with that username already exists.")},widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'User Name'}))
    first_name = forms.CharField(max_length=12, min_length=4, required=True, help_text='Required: First Name',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=12, min_length=4, required=True, help_text='Required: last Name',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))
    email = forms.EmailField(max_length=50, help_text='Required. Inform a valid email address.',widget=(forms.TextInput(attrs={'class': 'form-control','placeholder':'Email'})))
    password1 = forms.CharField(label=('Password'),widget=(forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Password'})),help_text=('password_validation.password_validators_help_text_html'))
    password2 = forms.CharField(label=('Password Confirmation'), widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Retype Password'}),help_text=('Just Enter the same password, for confirmation'))
    class Meta:
        model = User
        # fields = '__all__'
        fields = ('username','first_name','last_name','email' ,'password1','password2') 