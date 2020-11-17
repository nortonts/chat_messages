import json

from django.shortcuts import render
from django.utils.safestring import mark_safe


def index(request):
    """Главная страница"""
    room_name = 'index'
    return render(request, 'index.html', {'room_name': room_name})

def chat(request, room_name):
    return render(request, 'chat.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })

def room(request, room_name):
    """"""
    return render(request, 'room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })
