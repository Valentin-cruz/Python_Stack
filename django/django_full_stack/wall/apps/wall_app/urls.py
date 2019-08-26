from django.conf.urls import url, include
from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.index),
    path('adduser', views.reg_valid),
    path('users', views.log_valid),
    path('wall', views.home),
    path('addmessage', views.addmessage),
    path('message/<id>/delete', views.deletemessage),
    path('addcomment', views.addcomment),
    path('logout', views.logout)
]