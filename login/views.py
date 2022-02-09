from django.shortcuts import render
from django.template import loader
import subprocess

def login(request):
    context = {}
    if 'loggedIn' not in request.session:
        return render(request, 'login/login.html', context)
    else:
        return render(request, 'login/test.html', context)
