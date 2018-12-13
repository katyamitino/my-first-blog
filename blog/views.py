from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.utils import timezone
from .models import Product, Client, Order, Supplier
from .forms import ProductForm, ClientForm, OrderForm, SupplierForm
from django.http import HttpResponseRedirect
from django.db.models import Q, Max, Min, Avg, Count
from django.contrib.auth.decorators import login_required

#for PRODUCT
def product_list(request):
    products = Product.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/product_list.html', {'products': products})

def product_list_order_by_name(request):
    products = Product.objects.order_by('name')
    return render(request, 'blog/product_list.html', {'products': products})

def product_list_ascending_order(request):
    products = Product.objects.order_by('price')
    return render(request, 'blog/product_list.html', {'products': products})

def product_list_descending_order(request):
    products = Product.objects.order_by('-price')
    return render(request, 'blog/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'blog/product_detail.html', {'product': product})

def product_new(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.author = request.user
            product.published_date = timezone.now()
            product.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm()
    return render(request, 'blog/product_edit.html', {'form': form})

def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.author = request.user
            product.published_date = timezone.now()
            product.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm(instance=product)
    return render(request, 'blog/product_edit.html', {'form': form})

def product_delete(request, pk):
        product = Product.objects.get(pk=pk)
        product.delete()
        return HttpResponseRedirect("/")


#for CLIENTS
def client_list(request):
    clients = Client.objects.order_by('fio')
    return render(request, 'blog/client_list.html', {'clients': clients})

def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    clientfio = client.fio
    order_clients = Order.objects.filter(fio__icontains = clientfio)
    return render(request, 'blog/client_detail.html',
     {'client': client,'order_clients': order_clients} )

def client_new(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.author = request.user
            client.published_date = timezone.now()
            client.save()
            return redirect('client_detail', pk=client.pk)
    else:
        form = ClientForm()
    return render(request, 'blog/client_edit.html', {'form': form})

def client_edit(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            client = form.save(commit=False)
            client.author = request.user
            client.published_date = timezone.now()
            client.save()
            return redirect('client_detail', pk=client.pk)
    else:
        form = ClientForm(instance=client)
    return render(request, 'blog/client_edit.html', {'form': form})

def client_delete(request, pk):
        client = Client.objects.get(pk=pk)
        client.delete()
        return HttpResponseRedirect("/client_list/")

#for ORDERS
def order_list(request):
    orders = Order.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/order_list.html', {'orders': orders})

def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'blog/order_detail.html', {'order': order})

def order_new(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.author = request.user
            order.published_date = timezone.now()
            order.save()
            return redirect('order_detail', pk=order.pk)
    else:
        form = OrderForm()
    return render(request, 'blog/order_edit.html', {'form': form})

def order_edit(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            order = form.save(commit=False)
            order.author = request.user
            order.published_date = timezone.now()
            order.save()
            return redirect('order_detail', pk=order.pk)
    else:
        form = OrderForm(instance=order)
    return render(request, 'blog/order_edit.html', {'form': form})

def order_delete(request, pk):
        order = Order.objects.get(pk=pk)
        order.delete()
        return HttpResponseRedirect("/order_list/")

#for SUPPLIERS
def supplier_list(request):
    suppliers = Supplier.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/supplier_list.html', {'suppliers': suppliers})

def supplier_detail(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    return render(request, 'blog/supplier_detail.html', {'supplier': supplier})

def supplier_new(request):
    if request.method == "POST":
        form = SupplierForm(request.POST)
        if form.is_valid():
            supplier = form.save(commit=False)
            supplier.author = request.user
            supplier.published_date = timezone.now()
            supplier.save()
            return redirect('supplier_detail', pk=supplier.pk)
    else:
        form = SupplierForm()
    return render(request, 'blog/supplier_edit.html', {'form': form})

def supplier_edit(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == "POST":
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            supplier = form.save(commit=False)
            supplier.author = request.user
            supplier.published_date = timezone.now()
            supplier.save()
            return redirect('supplier_detail', pk=supplier.pk)
    else:
        form = SupplierForm(instance=supplier)
    return render(request, 'blog/supplier_edit.html', {'form': form})

def supplier_delete(request, pk):
        supplier = Supplier.objects.get(pk=pk)
        supplier.delete()
        return HttpResponseRedirect("/supplier_list/")


def statistics(request):
    max_price = Product.objects.all().aggregate(Max('price'))['price__max']
    need = Product.objects.get(price = max_price)
    min_price = Product.objects.all().aggregate(Min('price'))['price__min']
    minimum = Product.objects.get(price = min_price)
    avg_price = Product.objects.all().aggregate(Avg('price'))['price__avg']
    count = Product.objects.count()
    return render(request, 'blog/statistics.html', {'max_price': max_price,
    'min_price': min_price, 'avg_price': avg_price, 'count': count, 'need':need,
    'minimum': minimum, })

def search_form(request):
    return render_to_response('product_list.html')

def search(request):
    if 't' in request.GET and request.GET['t']:
        t = request.GET['t']
        products = Product.objects.filter(Q(name__icontains=t)|Q(price__icontains=t)
        |Q(number__icontains=t)|Q(supplier__icontains=t))
        clients = Client.objects.filter(Q(fio__icontains=t)|Q(company__icontains=t)
        |Q(phone_number__icontains=t)|Q(order_id__icontains=t))
        orders = Order.objects.filter(Q(fio__icontains=t)|Q(company__icontains=t)
        |Q(phone_number__icontains=t))
        suppliers = Supplier.objects.filter(Q(company__icontains=t)
        |Q(phone_number__icontains=t)|Q(address__icontains=t)|Q(description__icontains=t))
        return render_to_response('blog/search_results.html',
            {'products': products,'clients': clients, 'orders': orders,
             'suppliers': suppliers,'query': t})

def count_prod(request):
    count_prod = Product.objects.count()
    return render(request, 'blog/product_list.html', {'count_prod': count_prod})

def passport_form(request):
    return render_to_response('blog/passport.html')

def passport(request):
    if 'a' in request.GET and request.GET['a']:
        a = request.GET['a']
        products = Product.objects.filter(Q(id__icontains=a)|Q(name__icontains=a))
        return render_to_response('blog/passport.html',
            {'products': products,'querya': a})
