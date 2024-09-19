from django.db import models

class Customer(models.Model):
    first_name = models.CharField("First name", max_length=255)
    last_name = models.CharField("Last name", max_length=255)
    email = models.CharField("email", max_length=255)
    phone = models.CharField("Phone number", max_length=20)
    address = models.CharField("Address", max_length=255, blank=True, null=True)  # Add max_length here
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return self.first_name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
