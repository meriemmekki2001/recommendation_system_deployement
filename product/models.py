from django.db import models
from django.utils.translation import gettext_lazy as _



class Product(models.Model):
    stock_code = models.CharField(_("stock code"), max_length=50,blank=True,null=True)
    title = models.CharField(max_length=250)
    price = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    quantity = models.IntegerField(default=10)
    image = models.ImageField(upload_to='product_pics', blank=True, null=True)

 
