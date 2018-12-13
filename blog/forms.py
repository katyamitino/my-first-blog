from django import forms
from .models import Product
from .models import Client, Order, Supplier

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name','price','number','supplier',)

class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ('fio','company','phone_number','order_id',)

class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('fio','company','phone_number','order',)

class SupplierForm(forms.ModelForm):

    class Meta:
        model = Supplier
        fields = ('company','phone_number','address', 'description',)

class SearchForm(forms.Form):
    query = forms.CharField()
