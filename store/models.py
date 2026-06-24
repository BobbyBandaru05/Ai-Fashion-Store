from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):

    CATEGORY_CHOICES = [
    ('Men', 'Men'),
    ('Women', 'Women'),
    ('Accessories', 'Accessories'),
] 

    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='products/')

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Men')

    brand = models.CharField(max_length=100, blank=True)
    rating = models.FloatField(default=4.5)
    reviews = models.IntegerField(default=0)
    color = models.CharField(max_length=100, blank=True)
    size = models.CharField(max_length=100, blank=True)
    material = models.CharField(max_length=100, blank=True)
    stock = models.IntegerField(default=0)
    offer = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    quantity = models.IntegerField(default=1)
    total_price = models.FloatField()

    status = models.CharField(max_length=50, default="Pending")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"