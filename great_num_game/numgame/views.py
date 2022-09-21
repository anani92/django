from django.shortcuts import render, redirect
import random


def guess_game(request):
    random_num = random.randint(1, 101)
    if 'num' not in request.session:
        request.session['num'] = random_num

    return render(request, 'numgame/index.html')


def context(text, color):
    box_text = text
    box_color = color
    context = {
        'text': box_text,
        'color': box_color
    }
    return context


def play(request):
    random_num = request.session['num']
    guess = request.POST['guess']
    guess = int(guess)

    if guess == random_num:
        request.session.clear()
        return render(request, 'numgame/index.html', context('wow you guessed it right', 'green'))
    if guess < random_num:
        return render(request, 'numgame/index.html', context('too Low', 'blue'))
    if guess > random_num:
        return render(request, 'numgame/index.html', context('too High', 'red'))
