
from django.core.checks.messages import Error
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import View
from store.models.product import Product

class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        return render(request, 'cart.html', {'products': products})


       
