from django.shortcuts import render
from .models import Product

# Create your views here.
def shophome(request):
    products=Product.get_all_products()
    print(products)

    return render(request, 'Shop/shophome.html', {'Products':products})


