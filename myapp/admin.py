from django.contrib import admin
from .models import MyApp

class MyAppAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname')

admin.site.register(MyApp, MyAppAdmin)
