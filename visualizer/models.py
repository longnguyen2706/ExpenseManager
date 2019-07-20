from django.db import models

# Create your models here.

class SuperStore(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.CharField(max_length=200)
    order_date = models.DateField()
    ship_date = models.DateField()
    ship_mode = models.CharField(max_length=200)
    customer_id = models.CharField(max_length=200)
    customer_name = models.CharField(max_length=1000)
    segment = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    postal_code = models.IntegerField()
    region = models.CharField(max_length=50)
    product_id = models.CharField(max_length=200)
    category = models.CharField(max_length =50)
    sub_category = models.CharField(max_length=50)
    product_name = models.CharField(max_length = 1000)
    sales = models.DecimalField(decimal_places=5, max_digits=10)
    quantity = models.IntegerField()
    discount = models.DecimalField(decimal_places=2,max_digits=2)
    profit = models.DecimalField(decimal_places=5, max_digits=10)

