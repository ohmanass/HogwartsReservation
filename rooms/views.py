from django.shortcuts import render
from django.http import JsonResponse
from myproject import ROOMS_DICT

# Create your views here.

def get_rooms(request):
    return JsonResponse(ROOMS_DICT)