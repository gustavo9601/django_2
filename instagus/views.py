"""
InstaGus Views
"""
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, JsonResponse
import pdb

from datetime import datetime


def hello_world(request: WSGIRequest) -> HttpResponse:
    print(request.headers)
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse(f"Hello World Initial at {now} !!!")


def params_query(request: WSGIRequest) -> HttpResponse:
    # pdb.set_trace()  // debug por consola

    # Accediendo a variables queries GET
    print(request.GET)
    name = request.GET['name']
    age = request.GET['age']
    years = sorted(request.GET['years'].split(','))
    return JsonResponse({
        "name": name,
        "age": age,
        "years": years
    })


def params_url(request: WSGIRequest, name: str, age: int):
    return JsonResponse({
        "name": name,
        "age": age,
    })
