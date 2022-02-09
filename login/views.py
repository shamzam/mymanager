from django.shortcuts import render
from django.template import loader
import subprocess

def login(request):
    context = []
    
    return render(request, 'login/login.html', context)
