from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import LoginForm
from register.forms import forms
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

# Create your views here.


def home_view(request):
    return render(request, 'galleria/main.html')


def signin(request):
    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect('/')
            else:
                messages.error(request,"Your account was inactive.")
                return redirect('/login/')
        else:
            messages.error(request,"Invalid username or password.")
            return redirect('/login/')
    else:
        return render(request, 'login/login.html', {})

def signout(request):
    logout(request)
    return redirect('/')
