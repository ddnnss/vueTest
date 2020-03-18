import json

from django.http import JsonResponse
from django.shortcuts import render
from .models import *
# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def index(request):
    items = Item.objects.all()
    return render(request, 'test.html', locals())

@csrf_exempt
def entry(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    Item.objects.create(name=body['fname'])
    items= Item.objects.all()
    response = []
    for i in items:
        response.append({'id': i.id,'text': i.name})




    return JsonResponse(response,safe=False)