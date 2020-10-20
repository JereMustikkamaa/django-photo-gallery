from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm

# Create your views here.


def home_view(request):
    return render(request, 'galleria/main.html')


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = RegisterForm()
    return render(request, "register/register.html", {"form": form})
