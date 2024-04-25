from django.db import models

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    dicount_price = models.FloatField()
    category = models.CharField(max_length=100)
    description = models.TextField()
    image = models.CharField(max_length=300)

    def __str__(self):
        return self.title

class Orders(models.Model):
    items = models.TextField(max_length=1000)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    address = models.TextField(max_length=1000)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)
    total = models.CharField(max_length=200,default=" ")

    def __str__(self):
        return self.name