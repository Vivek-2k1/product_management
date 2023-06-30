from django.db import models

# Create your models here.
class ProductModel(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class CategoryModel(models.Model):
    name = models.CharField(max_length=40)
    products = models.ManyToManyField(ProductModel)
    
    def __str__(self):
        return self.name