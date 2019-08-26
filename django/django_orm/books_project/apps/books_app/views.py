from django.shortcuts import render, redirect, HttpResponse
from apps.books_app.models import *

def books(request):
    data={
        'books': Books.objects.all()
    }
    return render(request,'books_app/books.html', data)

def addbook(request):
    data = {
        'book':Books.objects.get(id=request.POST['bookid']),
        'author':Authors.objects.get(id=request.POST['authorid']),
    }
    data['author'].books.add(data['book'])
    return redirect('/author/'+str(data['author'].id))

def newbook(request):
    data={
        "book": request.POST
    }
    Books.objects.create(title=data['book']['title'],desc=data['book']['description'])
    return redirect('/')

def book(request,id):
    context ={
        'book': Books.objects.get(id=id),
        'authors': Authors.objects.all()
    }
    return render(request,'books_app/book.html',context)

def authors(request):
    data = {
        'authors': Authors.objects.all()
    }
    return render(request,'books_app/authors.html', data)

def newauthor(request):
    data = {
        'first_name': request.POST['first_name'],
        'last_name': request.POST['last_name'],
        'notes': request.POST['notes'],
    }
    Authors.objects.create(first_name=data['first_name'], last_name =data['last_name'],notes=data['notes'])
    return redirect('/authors')

def addauthor(request):
    data = {
        'book':Books.objects.get(id=request.POST['bookid']),
        'author':Authors.objects.get(id=request.POST['authorid']),
    }
    data['book'].authors.add(data['author'])
    return redirect('/book/'+str(data['book'].id))

def author(request,id):
    data = {
        'author': Authors.objects.get(id=id),
        'books': Books.objects.all()
    }
    return render(request,'books_app/author.html',data)