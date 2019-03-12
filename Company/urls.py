from django.urls import path

from Company import views


# from main.views import main
urlpatterns = [
    path('', views.show_company)
]