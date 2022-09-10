from os import name
from .views import home_page, log_out, login_request, dashboard_page
from django.urls import path

app_name = 'PenaltyManager'

urlpatterns = [
    path('', home_page, name='home'),
    path('login/', login_request, name='login'),
    path('logout/', log_out, name='logout'),
    path('dashboard/', dashboard_page, name='dashboard')
]