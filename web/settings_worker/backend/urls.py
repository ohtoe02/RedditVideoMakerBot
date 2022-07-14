from django.urls import path
from .views import get, update
urlpatterns = [
    path('', get),
    path('update', update),
]