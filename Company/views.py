from django.shortcuts import render

# Create your views here.

def show_company(request):
    return render(request,'company/company.html')