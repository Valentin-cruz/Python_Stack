from django.conf.urls import url
from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.index),
    path('dashboard', views.dashboard),
    path('home', views.home),
    path('adduser', views.login),
    path('users', views.login),
    path('products', views.products),
    path('cart', views.shopcart),
    path('item', views.item),
    path('search', views.do_search),
]