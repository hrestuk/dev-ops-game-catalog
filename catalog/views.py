from django.shortcuts import render
from .models import Game


def home(request):
    return render(request, 'catalog/home.html')


def game_list(request):
    games = Game.objects.all()
    return render(
        request,
        'catalog/game_list.html',
        {'games': games}
    )