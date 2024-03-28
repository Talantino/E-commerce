from django.db import models
from customers.models import User
from products.models import Product
from shipping_and_billing.models import Address
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator


class Order(models.Model):
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
    payment_method = models.CharField(max_length=4, choices=PAYMENT_METHOD_CHOICES)
    discount_applied = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])

    def update_total_price(self):
        self.total_price = sum(item.get_total_price() for item in self.details.all())
        self.save()

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return f"Order by {self.user}"


class OrderDetails(models.Model):
    order = models.ForeignKey("Order", on_delete=models.CASCADE, related_name="details")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price_at_purchase = models.DecimalField(max_digits=10, decimal_places=2)

    def get_total_price(self):
        return self.quantity * self.price_at_purchase

    class Meta:
        verbose_name = "Order Details"
        verbose_name_plural = "Order Details"

    def __str__(self):
        return f"Order details of the {self.order}"


@receiver(post_save, sender=OrderDetails)
def update_order_total(sender, instance, **kwargs):
    instance.order.update_total_price()

    """
    Whenever an OrderDetails instance is saved, it triggers the update_order_total function, 
    which then calls the update_total_price method
    on the related Order instance to recalculate the total price. 
    This ensures that the total_price on the Order is always up to date after adding or modifying an order detail.
    """
