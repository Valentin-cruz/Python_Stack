# create your_project_name_here
(djangoPy3Env) > cd python_stack/django/django_intro
(djangoPy3Env) django_intro> django-admin startproject your_project_name_here

# run project
(djangoPy3Env) django_intro> cd your_project_name_here
(djangoPy3Env) your_project_name_here> python manage.py runserver

# create apps folder
(djangoPy3Env) your_project_name_here> mkdir apps
# // THIS STEP CAN ALSO BE DONE BY MANUALLY CREATING A FILE USING A USER INTERFACE OF SOME KIND, SUCH AS THE FILE CREATION BUTTON IN VSCODE

# create django app
(djangoPy3Env) apps> python ../manage.py startapp your_app_name_here
# The apps in a project CANNOT have the same name as the project.

# add url.py to django app
(djangoPy3Env) apps> cd app_name
(djangoPy3Env) your_app_name_here> touch urls.py

# add new app to setting.py
# your_project_name_here/your_project_name_here/settings.py
    INSTALLED_APPS = [
        'apps.your_app_name_here', # added this line. Don't forget the comma!!
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]    # the trailing comma after the last item in a list, tuple, or dictionary is commonly accepted in Python

# add url pattern
# your_project_name_here/your_project_name_here/urls.py
from django.conf.urls import url, include	# added an import!
# from django.contrib import admin              # comment out, or just delete
urlpatterns = [
    url(r'^', include('apps.your_app_name_here.urls')),	# use your app_name here
    # url(r'^admin/', admin.sites.urls)         # comment out, or just delete
]

# add to app url.py
# your_project_name_here/apps/your_app_name_here/urls.py
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

# add function to app's view.py file
# your_project_name_here/apps/your_app_name_here/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
import re
import bcrypt
from .models import User

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

def index(request):
    if 'login' not in request.session:
        request.session['login'] = False
    if 'user_id' not in request.session:
        request.session['user_id'] = 0
    return render(request, 'python_app/index.html')

# session
(djangoPy3Env) project_name> python manage.py migrate

# run django project
(djangoPy3Env) your_project_name_here> python manage.py runserver


# ----------------------------------------
# migration
    > python manage.py makemigrations
    > python manage.py migrate

# Django shell
    > python manage.py shell

#  -------------------------------
# static files
{% load static %}
    <link rel="stylesheet" href=copy"{% static 'app_name/css/style.css' %}">    
    <script src="{% static 'app_name/js/script.js' %}"></script>
    <body>
        <img src="{% static 'app_name/images/image.jpg' %}" />
    </body>