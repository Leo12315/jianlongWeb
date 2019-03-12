"""jianlongWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Home.views import show_home
from Company.views import show_company
from Product.views import show_product
from Team.views import show_team
from News.views import show_news
from Joinus.views import show_joinus


urlpatterns = [
    path('home/',show_home),
    path('company/',show_company),
    path('product/',show_product),
    path('team/',show_team),
    path('news/',show_news),
    path('joinus/',show_joinus)
]
