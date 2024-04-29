from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from . import models
# Create your views here.

def home(request):
    return render(request, "core/index.html")