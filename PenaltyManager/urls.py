from os import name
from .views import home_page, login_page, log_out
from django.urls import path

app_name = 'PenaltyManager'

urlpatterns = [
    path('', home_page, name='home'),
    path('login/', login_page, name='login'),
    path('logout/', log_out, name='logout'),
]