from django.conf.urls import url
from django.urls import path
from . import views
                    
urlpatterns = [
    path('shows', views.index),
    path('shows/new', views.newshow),
    path('shows/create', views.createshow),
    path('shows/<id>', views.show),
    path('shows/<id>/edit', views.editshow),
    path('shows/<id>/update', views.updateshow),
    path('shows/<id>/destroy', views.destroyshow),
]