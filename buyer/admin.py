from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Buyer

class BuyerAdmin(admin.ModelAdmin):
    list_display = ("customer_id","name","phone","email","loyalty_points")

admin.site.register(Buyer, BuyerAdmin)  
