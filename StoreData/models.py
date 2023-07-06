from django.db import models

class StoreData(models.Model):
   store_name = models.CharField(max_length = 50) 
   store_location =  models.CharField(max_length = 50)
   address = models.CharField(max_length = 50) 
   contact_information = models.CharField(max_length = 50)
   email = models.EmailField()
   
