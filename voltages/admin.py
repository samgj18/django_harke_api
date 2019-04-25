from django.contrib import admin
from voltages.models import UserData, Testing

@admin.register(UserData)
class UserData(admin.ModelAdmin):
    list_display = ('pk', 'voltage_coil_1', 'voltage_coil_2','voltage_generated_by_user','activity','datetime')

@admin.register(Testing)
class Testing(admin.ModelAdmin):
    list_display = ('voltage_coil_1', 'voltage_coil_2','voltage_generated_by_user','activity')