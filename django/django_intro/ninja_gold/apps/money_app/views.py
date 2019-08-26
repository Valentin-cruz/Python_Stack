from django.shortcuts import render, redirect, HttpResponse
import random
from datetime import datetime

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []
    return render(request,'money_app/index.html')

def money(request):
    if request.method == "POST":
        if request.POST['button'] == 'farm':
            gold = random.randint(10, 21)
            request.session['activities'].append('You are earned ' + str(gold) + ' golds from the ' + request.POST['button'] + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')

        elif request.POST['button'] == 'cave':
            gold = random.randint(5, 11)
            request.session['activities'].append('You are earned ' + str(gold) + ' golds from the ' + request.POST['button'] + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')

        elif request.POST['button'] == 'house':
            gold = random.randint(2,6)
            request.session['activities'].append('You are earned ' + str(gold) + ' golds from the ' + request.POST['button'] + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')
        
        elif request.POST['button'] == 'casino':
            gold = random.randint(-50, 51)
            if gold >= 0:
                request.session['activities'].append('Entered a casino and earned ' + str(gold) +' gold' + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')
            else:
                request.session['activities'].append('Entered a casino and lost ' + str(gold) + ' gold' + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')

        request.session['gold'] += gold
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')