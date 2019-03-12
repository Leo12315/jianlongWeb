from django.urls import path

from Team import views


# from main.views import main
urlpatterns = [
    path('', views.show_team)
]