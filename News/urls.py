from django.urls import path

from News import views


# from main.views import main
urlpatterns = [
    path('', views.show_news)
]