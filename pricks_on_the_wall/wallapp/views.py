from django.shortcuts import render, redirect
from .models import Message, Comment
from login.models import User

# Create your views here.


def home(request, id):
    user = User.objects.get(id=id)
    context = {
        'user': user,
        'messages': Message.objects.all(),
    }
    return render(request, 'home.html', context)


def write_message(request):
    text = request.POST.get('message')
    user_id = request.POST.get('user_id')
    print(user_id)
    user_created_message = User.objects.get(id=user_id)
    Message.objects.create(
        text=text,
        user=user_created_message
    )

    return redirect(f'/thewall/{user_id}')


def write_comment(request):
    user_id = request.POST.get('user_commented_id')
    user = User.objects.get(id=user_id)
    message_id = request.POST.get('message_id')
    message = Message.objects.get(id=message_id)
    comment_text = request.POST.get('comment')
    new_comment = Comment.objects.create(
        comment_text=comment_text,
        user=user,
        message=message,
    )
    new_comment.save()
    return redirect(f'/thewall/{user_id}')


def logout(request):
    request.session.clear()
    return redirect('/')
