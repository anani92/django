from django.shortcuts import render, redirect
import random


def game(request):
    if 'money' not in request.session:
        request.session['money'] = 1
    if 'activity_log' not in request.session:
        request.session['activity_log'] = []
    return render(request, 'goldgame/index.html')


def process_money(request):
    context = {
        "money": request.session['money'],
        'activity_log': request.session['activity_log']
    }
    money = random.randint(10, 21)
    casino = random.randint(1, 3)
    if request.POST['mine'] == 'farming':
        request.session['money'] += money
        request.session['activity_log'].append(
            f'<p class="text text-success">gained {money} from farming</p>')
    elif request.POST['mine'] == 'caving':
        request.session['money'] += money
        request.session['activity_log'].append(
            f'<p class="text text-success">gained {money} from caving</p>')
    elif request.POST['mine'] == 'looting':
        request.session['money'] += money
        request.session['activity_log'].append(
            f'<p class="text text-success">gained {money} from looting</p>')
    elif request.POST['mine'] == 'casino-play':
        casino_money = random.randint(10, 100)
        if casino == 1:
            request.session['money'] += casino_money
            request.session['activity_log'].append(
                f'<p class="text text-success">won {casino_money} from casino </p>')
        else:
            request.session['money'] -= casino_money
            request.session['activity_log'].append(
                f'<p class="text text-danger">lost {casino_money} from casino </p>')
    return render(request, 'goldgame/index.html', context)


def restart(request):
    request.session.clear()
    return redirect('/')
