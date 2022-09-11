from os import name
from .views import log_out, login_request, dashboard_page
from django.urls import path

app_name = 'PenaltyManager'

urlpatterns = [
    path('', login_request, name='login'),
    path('logout/', log_out, name='logout'),
    path('dashboard/', dashboard_page, name='dashboard')
]