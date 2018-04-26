from django.shortcuts import render
from django.views.generic.list import ListView
from django.utils import timezone
from django.views import generic

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

class BoardListView(ListView):

    model = Position
    paginate_by = 100  # if pagination is desired
    context_object_name = 'positions'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class PositionDetailView(generic.DetailView):
    model = Position
