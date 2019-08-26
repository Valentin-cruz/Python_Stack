from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
import re
import bcrypt
from .models import User
from .models import Message
from .models import Comment

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

def index(request):
    if 'login' not in request.session:
        request.session['login'] = False
    if 'user_id' not in request.session:
        request.session['user_id'] = 0
    return render(request, 'wall_app/index.html')

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
        return redirect('/wall')

def home(request):
    if request.session['login'] == True:
        data = {
        'user':User.objects.get(id=request.session['user_id']),
        'post_data':Message.objects.all(),
        'comment_data':Comment.objects.all(),
    }
    messages.success(request,'You are in.')
    return render(request, 'wall_app/wall.html',data)

def addmessage(request):
    Message.objects.create(message=request.POST['add_message'], user=User.objects.get(id=request.session['user_id']))
    messages.success(request,'Message posted successfully.')
    return redirect('/wall')

def deletemessage(request,id):
    message = Message.objects.get(id=id)
    print('-------',id)
    print(message)
    message.delete()
    return redirect('/wall')

def addcomment(request):
    Comment.objects.create(comment=request.POST['add_comment'],users_c=User.objects.get(id=request.session['user_id']),message_c=Message.objects.get(id=request.POST['message_id']) )
    messages.success(request,'Comment posted successfully.')
    return redirect('/wall')

def logout(request):
    request.session.clear()
    return redirect('/')