from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def list_posts(request: WSGIRequest):
    posts = [
        {
            'title': 'Mont',
            'user': {'name': 'Gus', 'picture': 'https://picsum.photos/200/300'},
            'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
            'picture': 'https://picsum.photos/200/300'
        }, {
            'title': 'Mont 2',
            'user': {'name': 'Gus 2', 'picture': 'https://picsum.photos/200/300'},
            'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
            'picture': 'https://picsum.photos/200/300'
        }
    ]
    # Retornando la vista
    return render(request, 'feed.html', {'posts': posts})
