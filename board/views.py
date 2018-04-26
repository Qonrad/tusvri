from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Position

"""
def index(request):
    return HttpResponse("Hello, world. You're at the board index.")
"""
def index(request):
    latest_position_list = Position.objects.order_by('-pub_date')[:5]
    output = ', '.join([p.description for p in latest_position_list])
    return HttpResponse(output)