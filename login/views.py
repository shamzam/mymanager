from django.shortcuts import render
from django.template import loader
import subprocess

def login(request):
    context = {}
    if request.session['loggedIn'] == True:
        return render(request, 'login/test.html', context)
    else:
        return render(request, 'login/login.html', context)
