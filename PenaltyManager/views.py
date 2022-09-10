# Importing required libraries
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Penalty, Driver
from django.contrib.auth.models import User
from .forms import LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.middleware import csrf
import json
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def home_page(request):
    context = {
        
    }
    return render(request, "PenaltyManager/login.html", context)

def dashboard_page(request):
    context = {

    }
    return render(request, "PenaltyManager/dashboard.html", context)

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
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

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect("PenaltyManager/dashboard.html")
			else:
				return redirect("/")
		else:
			print("Error")
	form = AuthenticationForm()
	return render(request=request, template_name="PenaltyManager/login.html", context={"form":form})

def log_out(request):
    logout(request)
    return redirect("/")
