from django.urls import path
from .views import *

urlpatterns = [
    path('',messageborad_view,name='messageboard'),
    path('subscribe/',subscribe, name='subscribe'),
    path('newsletter/',newsletter,name='newsletter'),
]