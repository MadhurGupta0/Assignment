import random
from django.shortcuts import render

quotes = [
    "The best way to predict the future is to invent it.",
    "Life is 10% what happens to us and 90% how we react to it.",
    "Your time is limited, don’t waste it living someone else’s life.",
    "Do what you can, with what you have, where you are.",
]

def home(request):
    random_quote = random.choice(quotes)
    return render(request, 'home.html', {
        'random_quote': random_quote,
    })

def index(request):
    text="This is this base for further use."
    return render(request, 'base.html',{"text":text})

