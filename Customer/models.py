from django.db import models

class Customer(models.Model):
   customer_id = models.AutoField(primary_key=True)
   name = models.CharField(max_length=50)
   phone = models.CharField(max_length=50)
   email = models.EmailField()
   loyalty_points = models.IntegerField()

