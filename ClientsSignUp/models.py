from django.db import models

# Create your models here.
class ClientsSignUp(models.Model):
   client_name = models.CharField(max_length=30)
   email = models.EmailField(max_length=50)
   first_name = models.CharField(max_length=30)
   last_name = models.CharField(max_length=30)
   phone_number = models.CharField(max_length=30)
   
   date_of_birth = models.DateField()
   
