from django.db import models
from customers.models import User
from products.models import Product
from shipping_and_billing.models import Address
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal


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
    discount_applied = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True, blank=True, default=0)

    def update_total_price(self):
        item_discounts = any(item.product.discount_flag for item in self.orderitems.all())
        if item_discounts:
            self.discount_applied = 15
        subtotal = sum(item.get_total_price() for item in self.orderitems.all())
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
        verbose_name = "Order-Details"
        verbose_name_plural = "Orders-Details"

    def __str__(self):
        return f"Order details {self.id} by {self.user}"


class OrderItem(models.Model):
    order = models.ForeignKey(OrderDetails, related_name="orderitems", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True)
    price_at_purchase = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

    def save(self, *args, **kwargs):
        price = self.product.price
        if self.product.discount_flag:
            price *= Decimal(0.85)
        self.price_at_purchase = price
        super().save(*args, **kwargs)

    def get_total_price(self):
        if self.quantity is None or self.price_at_purchase is None:
            return Decimal('0.00')
        return Decimal(self.quantity) * self.price_at_purchase

    class Meta:
        verbose_name = "Order Item"
        verbose_name_plural = "Order Items"

    def __str__(self):
        return f"Order items of the {self.product}"


@receiver(post_save, sender=OrderItem)
def update_order_total(sender, instance, **kwargs):
    instance.order.update_total_price()

