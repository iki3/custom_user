from django.shortcuts import render
from . import forms
from .models import InfoModelForm


# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'app_templates/index.html')
    
    

