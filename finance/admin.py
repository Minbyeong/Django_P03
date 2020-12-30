from django.contrib import admin

from .models import *

# Register your models here.
class FinanceAdmin(admin.ModelAdmin):
    list_display = ['year','mon','day']

admin.site.register(date_input, FinanceAdmin)