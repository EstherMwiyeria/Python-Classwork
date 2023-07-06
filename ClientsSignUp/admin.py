from django.contrib import admin


from .models import ClientsSignUp

class ClentsSignUpdmin(admin.ModelAdmin):
    list_display = ("client_name","email","first_name","last_name","date_of_birth","phone_number")

admin.site.register(ClientsSignUp, ClentsSignUpdmin) 
