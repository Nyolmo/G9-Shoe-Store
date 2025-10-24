from django.db import models
import uuid
from django.conf import settings
from products.models import Product
from django.utils import timezone

User = settings.AUTH_USER_MODEL

class Order(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    )

    order_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def calculate_total(self):
        """Recalculate total from related OrderItems"""
        return sum(item.price * item.quantity for item in self.items.all())

    def save(self, *args, **kwargs):
        # Save once first so related OrderItems exist in the DB
        super().save(*args, **kwargs)
        # Then update the total based on items
        total = self.calculate_total()
        if self.total != total:
            self.total = total
            super().save(update_fields=['total'])

    def __str__(self):
        return f"Order {self.order_id} - {self.user}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # ✅ Snapshots — store product info at purchase time
    product_name = models.CharField(max_length=255, blank=True)
    product_price_at_order = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def save(self, *args, **kwargs):
        # Preserve product data at time of order creation
        if not self.product_name:
            self.product_name = self.product.name
        if not self.product_price_at_order:
            self.product_price_at_order = self.product.price
        # Ensure price defaults to the product's current price
        if not self.price:
            self.price = self.product.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.quantity} x {self.product_name or self.product.name} for Order {self.order.order_id}"


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(default=timezone.now)
  # ✅ Track when added to cart

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in {self.user}'s cart"