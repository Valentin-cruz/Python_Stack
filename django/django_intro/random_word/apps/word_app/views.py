from django.shortcuts import render, redirect, HttpResponse
from django.utils.crypto import get_random_string

def index(request):
    return render(request,'word_app/index.html')

def r_word(request):
    if 'count' in request.session:
        request.session['count'] += 1
    else:
        request.session['count'] = 1
    
    random_word = get_random_string(length=14)
    word = {
        'random_word': random_word
    }
    print(random_word)
    return render(request, 'word_app/index.html', word)

def reset(request):
    request.session.clear()
    return redirect('/')

