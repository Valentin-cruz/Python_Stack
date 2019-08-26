from django.shortcuts import render, redirect
from django.contrib import messages
import re
import bcrypt
from .models import Show

def index(request):
    data={
        'shows': Show.objects.all()
    }
    return render(request, 'shows_app/index.html', data)

def newshow(request):
    return render(request, 'shows_app/addshow.html')

def createshow(request):
    return redirect('/shows/<id>')

def show(request):
    data={
        'shows':Show.objects.get(id=id)
    }
    return render(request, 'shows_app/show.html', data)

def editshow(request):
    return render(request, 'shows_app/editshow.html')

def updateshow(request):
    return redirect('/shows/<id>')

def destroyshow(request):
    User.objects.get(id=id).delete()
    return redirect('/shows')