from django.db import models

class Sale(models.Model):
    product_name = models.CharField(max_length=255)
    product_code = models.CharField(max_length=100)
    product_category = models.CharField(max_length=100)
    quantity_sold = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_date = models.DateField()

    def __str__(self):
        return f"{self.product_name} ({self.product_code}) - {self.quantity_sold} units"
