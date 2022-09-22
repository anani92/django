from django.shortcuts import render, redirect
import random
from time import strftime
from datetime import datetime


def game(request):
    if 'money' not in request.session:
        request.session['money'] = 1
    if 'activity_log' not in request.session:
        request.session['activity_log'] = []
    return render(request, 'goldgame/index.html')

# helper function


def banker(request, action):
    casino = random.randint(1, 3)
    now = datetime.now()
    money = random.randint(10, 21)
    current_time = now.strftime('%m/%d/%Y, %H:%M:%S')
    if request.POST['mine'] == action and action != 'casino-play':
        request.session['money'] += money
        request.session['activity_log'].append(
            f'<p class="text text-success">gained {money} from {action}({current_time}) </p>')
    elif request.POST['mine'] == 'casino-play':
        casino_money = random.randint(10, 100)
        if casino == 1:
            request.session['money'] += casino_money
            request.session['activity_log'].append(
                f'<p class="text text-success">won {casino_money} from casino ({current_time})</p>')
        else:
            request.session['money'] -= casino_money
            request.session['activity_log'].append(
                f'<p class="text text-danger">lost {casino_money} from casino ({current_time})</p>')
    else:
        print('action name not defined')


def process_money(request):
    context = {
        "money": request.session['money'],
        'activity_log': request.session['activity_log']
    }
    action = request.POST['mine']
    print(action)
    banker(request, action)

    return render(request, 'goldgame/index.html', context)


def restart(request):
    request.session.clear()
    return redirect('/')
