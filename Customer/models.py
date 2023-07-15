from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):

   user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
   customer_id = models.AutoField(primary_key=True)
   name = models.CharField(max_length=50)
   phone = models.CharField(max_length=50)
   email = models.EmailField()
   loyalty_points = models.IntegerField()



def register(self):
        self.save
def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False
def isExist(self):
        if Customer.objects.filter(email = self.email):
             return True
        return False




