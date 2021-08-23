from django.db import models
from django.conf import settings
from myprojectapp.models import Product


# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cart')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(verbose_name='quantity', default=0)
    add_datetime = models.DateTimeField(auto_now_add=True, verbose_name='time')
    total_sum = models.DecimalField(verbose_name='sum of the cart', default=0, decimal_places=2, max_digits=18)

    @property
    def product_cost(self):
        return self.product.price * self.quantity

    @property
    def total_quantity(self):
        _items = Cart.objects.filter(user=self.user)
        _total_quantity = sum(list(map(lambda x: x.quantity, _items)))
        return _total_quantity

    @property
    def total_cost(self):
        _items = Cart.objects.filter(user=self.user)
        _total_cost = sum(list(map(lambda x: x.product_cost, _items)))
        return _total_cost
