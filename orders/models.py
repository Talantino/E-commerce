from django.db import models
from customers.models import User
from products.models import Product
from shipping_and_billing.models import Address
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(null=True)
    price_at_purchase = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def get_total_price(self):
        price = self.product.price
        if self.product.discount_flag:
            price *= 0.85                        # this is for 15% discount
        return self.quantity * price

    class Meta:
        verbose_name = "Order Details"
        verbose_name_plural = "Order Details"

    def __str__(self):
        return f"Order details of the {self.product}"


class OrderDetails(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled')
    ]
    PAYMENT_METHOD_CHOICES = [
        ('Card', 'Card'),
        ('Cash', 'Cash')
    ]
    user = models.ForeignKey(User, related_name="orders", on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="details")
    order_date = models.DateTimeField(auto_now_add=True)
    shipping_address = models.ForeignKey(
        Address,
        related_name="shipping_address",
        on_delete=models.SET_NULL,
        null=True
    )
    billing_address = models.ForeignKey(
        Address,
        related_name="billing_address",
        on_delete=models.SET_NULL,
        null=True
    )
    total_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    discount_applied = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True, blank=True)

    def update_total_price(self):
        subtotal = sum(item.get_total_price() for item in self.order.all())
        if subtotal > 20000:
            self.discount_applied = 15  # 15% discount
        elif subtotal > 10000:
            self.discount_applied = 10  # 10% discount
        else:
            self.discount_applied = 0
        discount_amount = Decimal(self.discount_applied / 100) * Decimal(subtotal)
        self.total_price = subtotal - discount_amount
        self.save()

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return f"Order by {self.user}"


@receiver(post_save, sender=Order)
def update_order_total(sender, instance, **kwargs):
    instance.order.update_total_price()

    """
    Whenever an Order instance is saved, it triggers the update_order_total function
    """
