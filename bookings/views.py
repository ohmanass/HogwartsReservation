from django.shortcuts import render
from django.http import JsonResponse
from myproject import BOOKINGS_DICT

# Create your views here.

def get_bookings(request):
    return JsonResponse(BOOKINGS_DICT)