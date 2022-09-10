from os import name
from .views import home_page
from django.urls import path

import PenaltyManager

app_name = 'PenaltyManager'

urlpatterns = [
    path('', home_page, name='home'),
]