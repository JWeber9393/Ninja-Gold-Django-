from django.shortcuts import render, HttpResponse, redirect
import random
import math
from time import gmtime, strftime

def index(request):

    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activities_list' not in request.session:
        request.session['activities_list'] = []

    context = {}
    context['my_gold'] = request.session['gold']  

    return render(request, "ninja_gold_app/index.html", context)

def process_gold(request):
           
    if request.POST['location']=='farm':
        gold = random.randint(10,20)
    elif request.POST['location']=='cave':
        gold = random.randint(5,10)
    elif request.POST['location']=='house':
        gold = random.randint(2,5)
    elif request.POST['location']=='casino':
        gold = random.randint(-50,50)
    request.session['gold'] += gold

    if gold > 0:
        activity = {
            'log' : f"You gained "+str(gold)+" gold at "+request.POST['location']+". NOICE!",
            'color' : 'green'
        }

    if gold < 0:
        activity = {
            'log' : f"You lost "+str(abs(gold))+" gold at "+request.POST['location']+". That sucks...",
            'color' : 'red'
        }
    #If you have a list in your session, append operations don't get saved to the object
    temp_list = request.session['activities_list']
    temp_list.insert(0, activity) 
    request.session['activities_list'] = temp_list 
    

    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')

