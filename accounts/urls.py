from django.urls import path
from . import views
urlpatterns = [
    path("register/", views.register, name='register'),
    path("register1/", views.register1, name='register1'),
    path("login/", views.login, name='login'),
    path("login1/", views.login1, name='login1'),
    path("logout/", views.logout, name='logout'),
    path("logout1/", views.logout1, name='logout1'),
    path("rajshahi/", views.rajshahi, name='rajshahi'),
    path("rajshahi1/", views.rajshahi1, name='rajshahi1'),
]