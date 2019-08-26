from django.conf.urls import url
from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('adduser', views.reg_valid),
    path('users', views.log_valid),
    path('dashboard', views.home),
    path('logout', views.logout)
]