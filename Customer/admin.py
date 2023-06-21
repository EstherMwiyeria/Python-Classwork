from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ("customer_id","name","phone","email","loyalty_points")

admin.site.register(Customer, CustomerAdmin)    


