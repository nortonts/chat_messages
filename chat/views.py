import json

from django.shortcuts import render
from django.utils.safestring import mark_safe


def index(request):
    """Главная страница"""
    room_name = 'index'
    return render(request, 'index.html', {'room_name': room_name})

def chat(request, room_name):
    account = request.user
    return render(request, 'chat.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'account': mark_safe(json.dumps(account.username))
    })

def room(request, room_name):
    """"""
    return render(request, 'room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })
