from django.db import models
from django.utils import timezone


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    number = models.CharField(max_length=200)
    supplier = models.CharField(max_length=200)
    published_date = models.DateTimeField(
        blank=True, null=True)

def publish(self):
    self.published_date = timezone.now()
    self.save()

def __str__(self):
    return self.name

class Client(models.Model):
    fio = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    order_id = models.CharField(max_length=200)
    published_date = models.DateTimeField(
        blank=True, null=True)

def publish(self):
    self.published_date = timezone.now()
    self.save()

def __str__(self):
    return self.fio

class Order(models.Model):
    fio = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    order =  models.TextField()
    created_date = models.DateTimeField(
                default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

def publish(self):
    self.published_date = timezone.now()
    self.save()

def __str__(self):
    return self.fio

class Supplier(models.Model):
    company = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    description =  models.TextField()
    created_date = models.DateTimeField(
                default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

def publish(self):
    self.published_date = timezone.now()
    self.save()

def __str__(self):
    return self.company
# Create your models here.
