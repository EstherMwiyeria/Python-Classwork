from django.contrib import admin
from .models import StoreData

class StoreDataAdmin(admin.ModelAdmin):
    list_display = ("store_name","store_location","address","contact_information","email")
admin.site.register(StoreData,StoreDataAdmin)
