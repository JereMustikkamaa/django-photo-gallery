from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.


def home_view(request):
    return render(request, 'galleria/main.html')


def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, username)
                messages.info(request, f"You are logged in as {username}")
                return redirect('/')
            else:
                messages.info(request, "Username OR password is incorrect")
    form = AuthenticationForm()
    context = {}
    return render(request, 'galleria/login.html', context)


def signout(request):
    logout(request)
    messages.info(request, "Logged out!")
    return redirect('/')
