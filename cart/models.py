from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    session_id = models.CharField(max_length=100, unique=True, blank=True, null=True)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='cart',
        null=True,
        blank=True
    )

    def __str__(self):
        return f'Cart ID: {self.id} - Created at: {self.created_at}'

    def total_price(self):
        return sum(item.total_price() for item in self.cart_items.all())

    def total_items(self):
        return sum(item.quantity for item in self.cart_items.all())


class CartItem(models.Model):
    quantity = models.IntegerField(default=1)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')

    def __str__(self):
        return f'{self.product.name} x {self.quantity} - Cart ID: {self.cart.id}'

    def total_price(self):
        return int(self.product.price) * int(self.quantity)
