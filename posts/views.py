from django.shortcuts import render
from django.views.generic import ListView
from .models import Posts


class home(ListView):
     model = Posts