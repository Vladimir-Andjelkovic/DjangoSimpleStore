from django.db import models
from django.contrib.auth.models import User
from cart.models import Cart, CartItem
from products.models import Product


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('denied', 'Denied'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    ordered_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='orders')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f'Order ID: {self.id} - {self.name}'

    def save_order_items(self):
        cart_items = CartItem.objects.filter(cart=self.cart)
        for cart_item in cart_items:
            OrderItem.objects.create(
                quantity=cart_item.quantity,
                price=cart_item.product.price,
                order=self,
                product=cart_item.product
            )


class OrderItem(models.Model):
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product.name} x {self.quantity}'

    def total_price(self):
        return self.quantity * self.price
