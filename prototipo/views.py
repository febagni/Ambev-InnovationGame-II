from django.shortcuts import render

from prototipo.models import Tweets


def index(request):
    return render(request, 'index.html')

def filtros(request):
    return render(request, 'filtros.html')


def tweets(request):
    tweets = Tweets.objects.all()
    tweets1 = []
    tweets2 = []
    for i in range (len(tweets)):
        if i%2!=0:
            tweets1.append(tweets[i])
        else:
            tweets2.append(tweets[i])
    context = {
        'tweets1' : tweets1,
        'tweets2' : tweets2,
    }
    return render(request, 'tweets.html', context)
