from django.urls import path
from .views import MessageListView, add_message

urlpatterns = [
    path('', MessageListView.as_view(), name='list'),
    path('add/', add_message, name='add'),
]

