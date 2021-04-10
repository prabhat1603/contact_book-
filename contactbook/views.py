from django.shortcuts import render
from django.contrib.auth.models import User

def Home(request):
    return render(request, 'home.html', {'user' : User.objects.get(username=request.user)})

def Loggedout(request):
    return render(request, 'home.html')
