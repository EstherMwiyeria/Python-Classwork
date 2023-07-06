from django.contrib import admin

# Register your models here.
from .models import Delivery
class DeliveryAdmin(admin.ModelAdmin):
    list_display=("delivery_address","order","contact_number","delivery_date","time","cyclist_name")
admin.site.register(Delivery,DeliveryAdmin)
