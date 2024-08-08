from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_seller = models.BooleanField(default=False)
    is_buyer = models.BooleanField(default=True)
    cart = models.OneToOneField('products.Cart', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.username
