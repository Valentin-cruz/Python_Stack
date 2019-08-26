from django.conf.urls import url
from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.index),
    path('adduser', views.reg_valid),
    path('users', views.log_valid),
    path('dashboard', views.home),
    path('wish_items/<id>/add', views.addwish),
    path('wish_items/<id>/remove', views.removewish),
    path('wish_items/<id>/delete', views.delete),
    path('wish_items/create', views.newitem),
    path('wish_items/additem', views.additem),
    path('wish_items/<id>', views.wishitem),
    path('logout', views.logout)
]