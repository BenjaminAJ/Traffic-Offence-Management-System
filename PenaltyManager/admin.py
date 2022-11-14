from django.contrib import admin
from .models import Penalty, Officer
# Register your models here.

# admin.site.register(Penalty)
# admin.site.register(Driver)
admin.site.register(Officer)


class PenaltyAdmin(admin.ModelAdmin):
    list_display = ('penalty_id', 'driver_name', 'driver_license', 'vehicle_plate', 'address', 'officer_name')
admin.site.register(Penalty, PenaltyAdmin)