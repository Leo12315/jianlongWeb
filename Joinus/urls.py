from django.urls import path

from Joinus import views


# from main.views import main
urlpatterns = [
    path('', views.show_joinus)
]