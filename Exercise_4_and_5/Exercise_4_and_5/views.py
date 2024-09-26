import random
from datetime import datetime
from django.shortcuts import render,redirect
from .form import SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
quotes = [
    "The best way to predict the future is to invent it.",
    "Life is 10% what happens to us and 90% how we react to it.",
    "Your time is limited, don’t waste it living someone else’s life.",
    "Do what you can, with what you have, where you are.",
]

def home(request):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    random_quote = random.choice(quotes)
    return render(request, 'home.html', {
        'current_time': current_time,
        'random_quote': random_quote,
    })


def index(request):
    text="This is this base for further use."
    return render(request, 'base.html',{"text":text})

def signup(request):
    if request.method == "POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
        else:
            return render(request,'signup.html',{
                'form': form
            })
    form=SignUpForm()
    return render(request, 'signup.html',{
        'form': form
    })
@login_required
def lout(request):
    logout(request)
    return redirect('home')

@login_required
def profile(request):
    print(request.user.username)
    return render(request,'profile.html',{"user":request.user})
