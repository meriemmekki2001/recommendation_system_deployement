from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save



class Product(models.Model):
    stock_code = models.CharField(_("stock code"), max_length=50,blank=True,null=True)
    title = models.CharField(max_length=250)
    price = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    quantity = models.IntegerField(default=10)
    image = models.ImageField(upload_to='product_pics', default='product_pics/box.png')



class Cart(models.Model):
    user = models.OneToOneField(User, related_name="user_cart", on_delete=models.CASCADE)
    total = models.DecimalField( max_digits=10, decimal_places=2, default=0, blank=True, null=True)


@receiver(post_save, sender=User)
def create_user_cart(sender, created, instance, *args, **kwargs):
    if created:
        Cart.objects.create(user=instance)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name="cart_item", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="cart_product", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)




 











