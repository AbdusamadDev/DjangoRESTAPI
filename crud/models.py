from django.db import models

class ProductModel(models.Model):
    name = models.CharField(max_length=150)
    content = models.TextField(max_length=5000, blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return self.name + "\n" + self.content + "\n" + str(self.price) 
