from django.urls import path

from Product import views


# from main.views import main
urlpatterns = [
    path('', views.show_product)
]