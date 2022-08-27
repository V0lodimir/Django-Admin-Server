from django.contrib import admin
from .models import MyApps

class MyAppsAdmin(admin.ModelAdmin):
    list_display = ('car', 'model')

admin.site.register(MyApps, MyAppsAdmin)