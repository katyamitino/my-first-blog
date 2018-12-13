from django.contrib import admin
from .models import Product
from .models import Client
from .models import Order, Supplier

admin.site.register(Product)
admin.site.register(Client)
admin.site.register(Order)
admin.site.register(Supplier)
# Register your models here.
