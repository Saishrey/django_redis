from django.shortcuts import render
from django.core.cache import cache
from django.http import JsonResponse
from .models import *

# Create your views here.
def home(request):

    db = None

    if cache.get('fruits'):
        payload = cache.get('fruits')
        db = 'redis'
    else:
        objs = Fruits.objects.all()
        payload = [obj.fruit_name for obj in objs]
        db = 'sqlite'

        cache.set('fruits', payload)

    return JsonResponse({'status' : 200, 'db' : db, 'data' : payload})