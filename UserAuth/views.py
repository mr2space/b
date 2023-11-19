from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib import messages


# Create your views here.


def logUser(request):
    if request.method != 'POST':
        return render(request, "login/login.html")
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
        login(request,user)
        messages.success(request, f"welcome {user.username}")
        return redirect("/g")
    else:
        messages.error(request, "username or password not matched")
        return redirect('/auth')