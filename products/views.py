from django.shortcuts import render
from .models import Product

# Views listed below.

def all_products(request):
    """ This will show all products, sorting and search queries """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)