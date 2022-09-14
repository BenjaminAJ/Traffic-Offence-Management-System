from os import name
from .views import log_out, login_request, dashboard_page, destroy, offencelist
from django.urls import path

app_name = 'PenaltyManager'

urlpatterns = [
    path('', login_request, name='login'),
    path('logout/', log_out, name='logout'),
    path('dashboard/', dashboard_page, name='dashboard'),
    path('delete/<int:id>', destroy, name='delete'),
    path('offencelist/', offencelist, name="offencelist")
    ]