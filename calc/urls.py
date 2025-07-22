from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('add', views.add, name="add"),
    path('home1', views.home1, name="home1"),
    path('add1', views.add1, name="add1"),
]
