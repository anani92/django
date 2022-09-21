from django.shortcuts import render, redirect
import random


def guess_game(request):
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
    random_guess = random.randint(1, 101)
    if 'num' not in request.session and 'tries' not in request.session:
        request.session['num'] = random_guess
        request.session['tries'] = 0
    random_num = request.session['num']
    guess = request.POST['guess']
    guess = int(guess)
    if guess == random_num:
        request.session.clear()
        return render(request, 'numgame/index.html', context('wow you guessed it right', 'green'))
    elif guess < random_num and request.session['tries'] < 5:
        request.session['tries'] += 1
        return render(request, 'numgame/index.html', context('too Low', 'blue'))
    elif guess > random_num and request.session['tries'] < 5:
        request.session['tries'] += 1
        return render(request, 'numgame/index.html', context('too High', 'red'))
    if guess != random_num and request.session['tries'] >= 5:
        return render(request, 'numgame/index.html', context('Game over number of tries exceeded please restart the game', 'purple'))


def reset(request):
    request.session.clear()
    return redirect('/')
