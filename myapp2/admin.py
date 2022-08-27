from django.contrib import admin
from .models import MyApp2

class MyApp2Admin(admin.ModelAdmin):
    list_display = ('mobile', 'model')

admin.site.register(MyApp2, MyApp2Admin)