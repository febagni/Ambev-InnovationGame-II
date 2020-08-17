from django.shortcuts import render

from prototipo.models import Tweets


def index(request):
    return render(request, 'index.html')


def estatisticas(request):
    return render(request, 'estatisticas.html')


def tweets(request):
    tweets = Tweets.objects.all()
    context = {
        'tweets': tweets,
    }
    return render(request, 'tweets.html', context)
