from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^r_word$', views.r_word),
    url(r'^reset$', views.reset),
]