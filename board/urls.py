from django.urls import path

from . import views

from board.views import BoardListView

urlpatterns = [
    path('', BoardListView.as_view(), name='board-list'),
    #path('list/', BoardListView.as_view(), name='board-list'),
]