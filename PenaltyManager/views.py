# Importing required libraries
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Penalty, Driver
from django.contrib.auth.models import User
from .forms import LoginForm
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url
from django.contrib.auth import authenticate, login, logout
from django.middleware import csrf
import json

# Create your views here.

def home_page(request):
    context = {
        
    }
    return render(request, "base.html", context)


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    # print(request.user.is_authenticated)
    if form.is_valid():
        # print(form.cleaned_data)
        context["form"] = LoginForm()
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        print(request.user.is_authenticated)
        if user is not None:
            # print(request.user.is_authenticated)
            login(request, user)
            try:
                del request.session['guest_email_id']
            except:
                pass
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
            # A backend authenticated the credentials
                return redirect("/")
        else:
            # No backend authenticated the credentials
            print("Error")
    return render(request, "base.html", context)


def log_out(request):
    logout(request)
    return redirect("/")
