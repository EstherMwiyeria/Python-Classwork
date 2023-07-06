from django.db import models

# Create your models here.
class Delivery(models.Model):
    # id=models.PositiveIntegerField()
    delivery_address=models.CharField(max_length=34)
    order=models.CharField(max_length=45)
    contact_number=models.CharField(max_length=34)
    delivery_date=models.DateTimeField(auto_now_add=True)
    time=models.TimeField()
    cyclist_name=models.CharField(max_length=34)