from django.contrib import admin
from .models import Penalty, Officer
# Register your models here.

admin.site.register(Penalty)
# admin.site.register(Driver)
admin.site.register(Officer)