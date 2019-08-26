from django.shortcuts import render, redirect
from django.contrib import messages
import re
import bcrypt
from .models import User, Item, Wish

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

def index(request):
    if 'login' not in request.session:
        request.session['login'] = False
    if 'user_id' not in request.session:
        request.session['user_id'] = 0
    return render(request, 'python_app/index.html')

def reg_valid(request):
    check = User.objects.filter(email = request.POST['email'])
    error = False

    if len(request.POST['first_name'])< 2:
        messages.error(request,'First Name must be longer than 1 character')
        error = True
    if not NAME_REGEX.match(request.POST['first_name']):
        messages.error(request,'First Name must only contain A-Z characters')
        error = True
    if len(request.POST['last_name'])< 2:
        messages.error(request,'Last Name must be longer than 1 character')
        error = True
    if not NAME_REGEX.match(request.POST['last_name']):
        messages.error(request,'Last Name must only contain A-Z characters')
        error = True
    if not EMAIL_REGEX.match(request.POST['email']):
        messages.error(request,'Email is in an invalid format')
        error = True
    if check:
        messages.error(request,'Email has already been registered')
        error = True
    if request.POST['password'] != request.POST['confirm_password']:
        messages.error(request,'Passwords do not match')
        error = True
    if len(request.POST['password']) < 8 :
        messages.error(request,'Password must be 8 or more characters long')
    if error == True:
        return redirect('/')
    elif error == False:
        hashed = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        decode_hash = hashed.decode()
        User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = decode_hash)
        messages.success(request, 'You are registered')
        return redirect ('/')

def log_valid(request):
    check = User.objects.filter(email = request.POST['email'])
    error = False

    if not EMAIL_REGEX.match(request.POST['email']):
        messages.error(request,'Invalid Email')
        error = True
    else:
        if check:
            if check[0].email == request.POST['email']:
                if bcrypt.checkpw(request.POST['password'].encode(),check[0].password.encode()):
                    request.session['login'] = True
                    request.session['user_id'] = check[0].id
                else:
                    messages.error(request,'Invalid Credentials')
                    error = True
            else:
                messages.error(request,'Invalid Credentials')
                error = True
        else:
            messages.error(request,'Invalid Credentials')
            error = True

    if error == True:
        return redirect('/')
    elif error == False:
        return redirect('/dashboard')

def home(request):
    if request.session['login'] == True:
        user=request.session['user_id']
        data={
            'items': Item.objects.exclude(wishers__wisher_id=user),
            'wishes': Wish.objects.filter(wisher_id=user),
            'all': Wish.objects.all()
        }
    return render(request,'python_app/dashboard.html', data)

def additem(request):
    if request.method == 'POST':
        wish = request.POST['wish_name']
        if len(wish)>3:
            items=Item.objects.create(title=wish, user_id=request.session['user_id'])
            Wish.objects.create(wish_id=items.id, wisher_id=request.session['user_id'])
            return redirect('/dashboard')
        else:
            messages.error(request,'Iteam must be at least 3 characters')
            return redirect('/wish_items/create')

    return render(request,'python_app/create_item.html')

def newitem(request):
    if request.session['user_id']:
        data={
            'users':User.objects.all()
        }
        return render(request, 'python_app/create_item.html', data)
    else:
        return redirect('/')

def wishitem(request,id):
    data={
        'item': Item.objects.get(id=id),
        'wish': Wish.objects.filter(wish_id=id)
    }
    return render(request, 'python_app/wish_item.html', data)

def delete(request,id):
    Item.objects.get(id=id, user_id=request.session['user_id']).delete()
    return redirect('/dashboard')

def logout(request):
    request.session.clear()
    return redirect('/')

def addwish(request,id):
    Wish.objects.create(wish_id=id, wisher_id=request.session['user_id'])
    return redirect('/dashboard')

def removewish(request,id):
    Wish.objects.get(wish_id=id, wisher_id=request.session['user_id']).delete()
    return redirect('/dashboard')