from django.conf.urls import url
from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.index),
    path('adduser', views.reg_valid),
    path('users', views.log_valid),
    path('success', views.home),
    path('logout', views.logout)
]