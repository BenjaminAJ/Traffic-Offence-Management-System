from django.shortcuts import render

# Importing required libraries
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Penalty, Driver
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.middleware import csrf
import json

# Create your views here.

def home_page(request):
    context = {
        
    }
    return render(request, "base.html", context)


def loginUser(request):
    """Function for login view."""

    # If GET request
    if request.method == "GET":

        # Returning response with login html page
        response = render(request, "login.html")
        return responseHeadersModifier(response)

    # If POST request
    elif request.method == "POST":

        # Extracting data from POST request
        username = request.POST["userName"]
        password = request.POST["userPassword"]

        # Authenticating username password
        user = authenticate(request, username = username, password = password)

        # If user authenticated successfully and user returned
        if user is not None:

            # Logging in (session)
            login(request, user)

            # Returning response with index html page
            response = render(request, "index.html")
            return responseHeadersModifier(response)

        # If no user found, user credentials wrong
        else:

            # Failure message
            context = {
                "Failure": "Invalid credentials."
            }

            # Returning response
            response = render(request, "login.html", context)
            return responseHeadersModifier(response)

