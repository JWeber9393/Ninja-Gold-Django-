from django.shortcuts import render, HttpResponse, redirect
import random

def index(request):
    print('*'*100)
    print("this is the index route.")
    return render(request, "ninja_gold_app/index.html")

def process_gold(request):
    print('*'*100)
    print("this is the processing route.")

    if 'gold' not in request.session:
        request.session['gold'] = 0
    
    if request.POST['location']=='farm':
        gold = random.randint(10,20)
    if request.POST['location']=='cave':
        gold = random.randint(5,10)
    if request.POST['location']=='house':
        gold = random.randint(2,5)
    if request.POST['location']=='casino':
        gold = random.randint(-50,50)
    
    request.session['gold'] += gold
    print(request.session['gold'])

    return redirect('/')