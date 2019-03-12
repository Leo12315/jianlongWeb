from django.shortcuts import render

# Create your views here.

def show_joinus(request):
    return render(request,'joinus/joinus.html')