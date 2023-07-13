from django.shortcuts import render
from django.http import HttpRequest

from store.models import Product


def say_hello(request):
    query_set = Product.objects.filter(title__icontains='coffee')

    return render(request, 'hello.html', {'products': query_set})
