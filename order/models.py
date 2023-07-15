from django.db import models
from Customer.models import Customer
from cart.models import Cart
from delivery.models import Delivery

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    order_items = models.TextField()
    total_cost = models.DecimalField(max_digits=8,decimal_places=2)
    delivery_address = models.CharField(max_length=100)
    delivery_date = models.DateField()
    status = models.CharField(max_length=50)

    customer = models.ForeignKey(Customer, null= True, on_delete = models.CASCADE)
    cart = models.ForeignKey(Cart, null= True, on_delete = models.CASCADE)
    

    
    
    
    
