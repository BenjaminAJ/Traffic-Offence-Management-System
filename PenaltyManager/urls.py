from os import name
from .views import log_out, login_request, dashboard_page, destroy, PenaltyListView, RecentListView
from django.urls import path

app_name = 'PenaltyManager'

urlpatterns = [
    path('', login_request, name='login'),
    path('logout/', log_out, name='logout'),
    path('dashboard/', dashboard_page, name='dashboard'),
    path('delete/<int:pk>', destroy, name='delete'),
    # path('offencelist/', offencelist, name="offencelist")
    path('offencelist/', PenaltyListView.as_view(), name="offencelist"),
    path('recentlist/', RecentListView.as_view(), name="recentlist")
    ]