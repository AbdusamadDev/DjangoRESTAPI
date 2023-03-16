from django.db import models

class ProductModel(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(max_length=5000, blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=9.99)

    def __str__(self):
        return "Title: {}, Content: {}, Price: {}".format(self.title, self.content, self.price)
        
    @property
    def sales_price(self):
        return str(self.price)
    
    def get_discount(self):
        return "<Discount>"
