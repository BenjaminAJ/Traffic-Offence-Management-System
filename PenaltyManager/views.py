# Importing required libraries
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Penalty, Officer
from django.contrib.auth.models import User
from .forms import LoginForm, PenaltyForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.middleware import csrf
import json
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.list import ListView


# Create your views here.
class RecentListView(ListView):
    model = Penalty
    queryset = Penalty.objects.order_by('-date')[:10]
    template_name = 'PenaltyManager/recentlist.html'  # Specify your own template name/location


class PenaltyListView(ListView):
    model = Penalty
    template_name = 'PenaltyManager/offencelist.html'

def dashboard_page(request):
    if request.method == "POST":  
        form = PenaltyForm(request.POST)  
        if form.is_valid():   
            try:
                # driver_name= form.cleaned_data['driver_name']
                # print(driver_name)
                form.save()  
                return redirect('PenaltyManager:offencelist')
            except:
                pass   
    else:  
        form = PenaltyForm()  
    return render(request,'PenaltyManager/dashboard.html',{'form':form})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("PenaltyManager:dashboard")
            else:
                return redirect("/")
        else:
            print("Error")
    form = AuthenticationForm()
    return render(request=request, template_name="PenaltyManager/login.html", context={"form":form})

def log_out(request):
    logout(request)
    return redirect("/")

# def offencelist(request):  
#     penaltys = Penalty.objects.all()  
#     return render(request,"PenaltyManager/offencelist.html",{'penaltys':penaltys})  

def destroy(request, id):  
    penalty = Penalty.objects.get(id=id)  
    penalty.delete()  
    return redirect("PenaltyManager:dashboard")