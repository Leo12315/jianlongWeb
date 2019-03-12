from django.shortcuts import render

# Create your views here.

def show_product(request):
    return render(request,'product/product.html')